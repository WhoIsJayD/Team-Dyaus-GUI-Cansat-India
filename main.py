import csv
import datetime
import logging
import os
import random
import shutil
import sys
from pathlib import Path
import QSS_Resources_rc
import folium
import serial
import serial.tools.list_ports
import vtk
from PyQt5.QtCore import QTimer, QFileSystemWatcher, QUrl
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QHeaderView, QTableWidgetItem
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from ui_interface import *


def check_directory():
    if not os.path.exists("Flight_050_Data_Files"):
        try:
            os.mkdir("Flight_050_Data_Files")
        except Exception as e:
            print(e)
            print("--->  Error creating directory while initializing gui.")
    if not os.path.exists("Flight_050_Data_Files/flight_050.csv"):
        try:
            with open("Flight_050_Data_Files/flight_050.csv", "w") as csv_file:
                csv_file.write(
                    "ID,TIME,PACKET COUNT,ALTITUDE,PRESSURE,TEMPERATURE,VOLTAGE,GNSS TIME,"
                    "GNSS LONGITUDE,GNSS LATITUDE,GNSS ALTITUDE,CONNECTED SATELLITES,ACCEL X,ACCEL Y,ACCEL Z,ROLL,"
                    "PITCH,YAW,GYRO 1 SPIN RATE,GYRO 2 SPIN RATE,STATE,HUMIDITY,VELOCITY")
        except Exception as e:
            print(e)
            print("--->  Error creating .csv file.")


class OrientationDisplayWidget(QWidget):
    def __init__(self, parent=None):
        super(OrientationDisplayWidget, self).__init__(parent)

        # Create a VTK widget
        self.vtk_widget = QVTKRenderWindowInteractor(self)

        self.setLayout(QVBoxLayout())  # Set layout for the widget
        self.layout().addWidget(self.vtk_widget)

        # Create a renderer, render window, and interactor
        self.renderer = vtk.vtkRenderer()
        self.render_window = self.vtk_widget.GetRenderWindow()
        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()

        # Load STL file representing a cylinder
        self.reader = vtk.vtkSTLReader()
        self.reader.SetFileName("can.STL")
        self.reader.Update()

        # Get the output polydata from the reader
        self.camera = vtk.vtkCamera()
        self.polydata = self.reader.GetOutput()

        # Create a mapper and actor for the polydata
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputData(self.polydata)

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

        # Set the center of rotation at the central axis of the cylinder
        bounds = self.polydata.GetBounds()
        self.actor.SetOrigin((bounds[0] + bounds[1]) / 2, (bounds[2] + bounds[3]) / 2, (bounds[4] + bounds[5]) / 2)

        # Add the actor to the renderer
        self.renderer.AddActor(self.actor)

        # Set the background color of the renderer
        self.renderer.SetBackground(8 / 255, 18 / 255, 44 / 255)

        # Add the renderer to the render window
        self.render_window.AddRenderer(self.renderer)

        # Initialize the interactor
        self.interactor.Initialize()

    def update_orientation(self, accel_x, accel_y, accel_z):
        self.actor.SetOrientation(0.0, 0.0, 0.0)  
        self.actor.RotateX(accel_y)
        self.actor.RotateY(accel_x)
        self.actor.RotateZ(accel_z)
        self.vtk_widget.GetRenderWindow().Render()


class GuiWindow(QMainWindow):
    map_threshold = 5
    map_threshold_time = 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.Map_File_Watcher = self.CSV_File_Watcher = self.timer = self.ser = self.CsvData = self.table = \
            self.CsvHeader = self.progress_calculation = None
        check_directory()
        self.progress_state = 0
        self.progress_states = 8
        self.ui = GuiMainWindow()
        self.ui.setupUi(self)
        self.ui.MapFrame = QWebEngineView(self.ui.Map)
        self.ui.MapFrame.resize(0, 0)
        self.ui.PortDropdown.clear()
        self.ui.PortDropdown.addItems(availablePorts())
        self.setWindowIcon(QIcon("icons/logo.jpg"))

        self.ThreeDGraphObj = OrientationDisplayWidget(self.ui.ThreeDGraphWidget)
        # self.ThreeDGraphObj.setDisabled(True)
        self.MapPlotPoints = []
        self.ThreeDGraphPoints = []
        self.XAxisList = []
        self.AltitudeList = []
        self.TempList = []
        self.VoltageList = []
        self.SpeedList = []
        self.HumidityList = []
        self.PressureList = []
        # self.XAxisList = [0, 0]
        # self.AltitudeList = [0.0, 0.0]
        # self.TempList = [0.0, 0.0]
        # self.VoltageList = [0.0, 0.0]
        # self.SpeedList = [0.0, 0.0]
        # self.HumidityList = [0.0, 0.0]
        # self.PressureList = [0.0, 0.0]
        self.TableCreation()

        self.cleanup()

        try:
            self.ui.Start.clicked.connect(self.TelemetryStart)
        except Exception as e:
            print(e)
            print("----> Error Checking if the start button is clicked.")
        try:
            self.ui.Calibrate.clicked.connect(self.TelemetryCalibrate)
        except Exception as e:
            print(e)
            print("----> Error Checking if the calibrate button is clicked.")
        self.show()

    def UpdateMapWidget(self):
        try:
            self.ui.MapFrame.load(QUrl().fromLocalFile(os.path.abspath("Flight_050_Data_Files/flight_050.html")))
            self.ui.MapFrame.resize(1580, 800)
            self.ui.Lat_Text.setText(f"{str(self.MapPlotPoints[-1][0])} °")
            self.ui.Longi_Text.setText(f"{str(self.MapPlotPoints[-1][1])} °")

        except Exception as e:
            print(e)
            print("----> Error Updating Map Widget.")

    def loadCsvData(self):
        if os.path.exists("Flight_050_Data_Files/flight_050.csv"):
            with open("Flight_050_Data_Files/flight_050.csv", "r") as csv_file:
                reader = csv.reader(csv_file)
                self.CsvHeader = next(reader)
                self.CsvData = list(reader)
        else:
            with open("Flight_050_Data_Files/flight_050.csv", "w") as csv_file:
                csv_file.write(
                    "ID,TIME,PACKET COUNT,ALTITUDE,PRESSURE,TEMPERATURE,VOLTAGE,GNSS TIME,"
                    "GNSS LONGITUDE,GNSS LATITUDE,GNSS ALTITUDE,CONNECTED SATELLITES,ACCEL X,ACCEL Y,ACCEL Z,ROLL,"
                    "PITCH,YAW,GYRO 1 SPIN RATE,GYRO 2 SPIN RATE,STATE,HUMIDITY,VELOCITY")

    def populateCsvData(self):
        self.table.setRowCount(len(self.CsvData))
        for row, data_row in enumerate(self.CsvData):
            for col, data_col in enumerate(data_row):
                item = QTableWidgetItem(data_col)
                item.setForeground(QBrush(QColor("white")))
                item.setBackground(QBrush(QColor("black")))
                item.setTextAlignment(5)
                self.table.setItem(row, col, item)

    def TableCreation(self):

        self.loadCsvData()
        self.table = QTableWidget(self)
        self.table.setRowCount(len(self.CsvData))
        self.table.setColumnCount(len(self.CsvHeader))
        self.table.setHorizontalHeaderLabels(self.CsvHeader)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.populateCsvData()
        self.table.setParent(self.ui.CSV_Display_Frame)
        self.table.resize(1560, 855)
        self.show()

    def TelemetryStart(self):
        if self.ui.Start.text() == "Start":
            writeCsv("\n\n\n\n", "Flight_050_Data_Files/updateGraph.txt")
            writeCsv("\n\n\n\n", "Flight_050_Data_Files/updateTelemetry.txt")
            self.ui.Start.setText("Stop")
            backup_csv()
            baud_rate = self.ui.BaudDropdown.currentText()
            port = self.ui.PortDropdown.currentText()
            self.progress_state = 0
            self.progress_states = 8
            self.ser = Communication(port, baud_rate)
            if self.ser.dummyPlug is False:
                self.ser.write(2)
            sensor_working_data = self.ser.readSensorStatus()
            error_pos = {0: "RTC", 1: "IMU", 2: "PRESSURE", 3: "TEMP"}
            sensor_status_labels = {i: getattr(self.ui, f"{error_pos[i]}_TEXT") for i in range(4)}
            for i, label in sensor_status_labels.items():
                status = "Error!" if sensor_working_data[i] == '0' else "OK!"
                color = "red" if sensor_working_data[i] == '0' else "green"
                label.setText(status)
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(f"background-color: {color}")
            print("##### Sensor status: Ready")
            self.ui.RESET_TEXT.setText("Prog.")
            self.ui.RESET_TEXT.setStyleSheet("background-color: grey")
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_data)
            self.timer.setInterval(250)
            self.timer.start()

            file_path = "Flight_050_Data_Files/flight_050"
            self.CSV_File_Watcher, self.Map_File_Watcher = QFileSystemWatcher(
                [f"{file_path}.csv"]), QFileSystemWatcher([f"{file_path}.html"])
            self.CSV_File_Watcher.fileChanged.connect(self.loadCsvData)
            self.CSV_File_Watcher.fileChanged.connect(self.populateCsvData)
            self.ui.BaudDropdown.setDisabled(True)
            self.ui.PortDropdown.setDisabled(True)
            print("##### Starting Reading Data : Ready")
            communicationData = self.ser.readData()
            self.initDataUpdate(communicationData, self.XAxisList)
            self.update_data()

        else:
            self.timer.stop()
            self.ui.Start.setText("Start")
            file_path = "Flight_050_Data_Files/flight_050"
            self.loadCsvData()
            self.populateCsvData()
            self.CSV_File_Watcher.removePaths([f"{file_path}.csv"])
            self.Map_File_Watcher.removePaths([f"{file_path}.html"])
            backup_html()
            self.ui.BaudDropdown.setDisabled(False)
            self.ui.PortDropdown.setDisabled(False)
            self.progress_state = 0
            self.progress_states = 8

            if hasattr(self, 'ser') and not self.ser.isDummyMode():
                self.ser.close()

            self.cleanup()

    def TelemetryCalibrate(self):
        if not self.ser:
            logging.warning("Not connected to a serial port.")
            return

        calibration_command = 3
        try:
            with self.ser:
                self.ser.write(calibration_command)
                self.ser.timeout = 6
                self.ser.read(self.ser.in_waiting)
                self.ser.start()
                self.ser.timeout = None
        except OSError as e:
            logging.error(f"Error communicating with serial port: {e}")
            raise

    def cleanup(self):
        self.XAxisList = [0, 0]
        self.AltitudeList = [0, 0]
        self.TempList = [0, 0]
        self.VoltageList = [0, 0]
        self.SpeedList = [0, 0]
        self.HumidityList = [0, 0]
        self.PressureList = [0, 0]
        self.MapPlotPoints = []
        self.ThreeDGraphPoints = []
        self.ui.Altitude_Graph.clear()
        self.ui.Temperature_Graph.clear()
        self.ui.Voltage_Graph.clear()
        self.ui.Speed_Graph.clear()
        self.ui.Humidity_Graph.clear()
        self.ui.Pressure_Graph.clear()
        self.ui.AltitutdePlaceholder.clear()
        self.ui.TemperaturePlaceholder.clear()
        self.ui.VoltagePlaceholder.clear()
        self.ui.SpeedPlaceholder.clear()
        self.ui.HumidityPlaceholder.clear()
        self.ui.PressurePlaceholder.clear()
        self.ui.LatitudePlaceholder.clear()
        self.ui.LongitudePlaceholder.clear()
        self.ui.TelemetryDummyValues.clear()
        self.ui.MissionTimePlaceholder.clear()
        self.ui.TimePlaceholder.clear()
        self.ui.GPSAltitudePlaceholder.clear()
        self.ui.ConnectedStatePlaceholder.clear()
        self.ui.ConnectedStatePlaceholder.clear()
        self.ui.DatePlaceholder.clear()
        self.ui.PacketCountPlaceholder.clear()
        self.ui.AccelerometerRoll.clear()
        self.ui.ACCElXPlaceholder.clear()
        self.ui.ACCElYPlaceholder.clear()
        self.ui.AccelerometerPitch.clear()
        self.ui.ACCElZPlaceholder.clear()
        self.ui.AccelerometerYaw.clear()
        self.ui.RTC_TEXT.clear()
        self.ui.IMU_TEXT.clear()
        self.ui.PRESSURE_TEXT.clear()
        self.ui.TEMP_TEXT.clear()
        self.ui.RESET_TEXT.clear()

        error_pos = {0: "RTC", 1: "IMU", 2: "PRESSURE", 3: "TEMP", 4: "RESET"}
        sensor_status_labels = {i: getattr(
            self.ui, f"{error_pos[i]}_TEXT") for i in range(5)}
        for i, label in sensor_status_labels.items():
            color = "#0F1830"
            label.setStyleSheet(f"background-color: {color}")

        self.ui.Altitude_Graph_Text.setText("Altitude :")
        self.ui.Temperature_Graph_Text.setText("Temperature :")
        self.ui.Voltage_Graph_Text.setText("Voltage :")
        self.ui.Speed_Graph_Text.setText("Velocity :")
        self.ui.Humidity_Graph_Text.setText("Humidity :")
        self.ui.Pressure_Graph_Text.setText("Pressure :")
        self.ui.SpinDial1Placeholder.setText("Gyro 1 : ")
        self.ui.SpinDial2Placeholder.setText("Gyro 2 : ")
        self.ui.ProgressStateDisplay.setText("Not Connected")
        self.ui.ProgressStateBar.setValue(0)
        self.ui.GPS_Map_Altitude_Placeholder.clear()
        self.ui.Lat_Text.clear()
        self.ui.Longi_Text.clear()

    def initDataUpdate(self, data, x_axis):
        try:
            self.XAxisList.append(int(x_axis[-1] + 1))
            self.AltitudeList.append(float(data["ALTITUDE"]))
            self.TempList.append(float(data["TEMPERATURE"]))
            self.VoltageList.append(float(data["VOLTAGE"]))
            self.SpeedList.append(float(data["VELOCITY"]))
            self.HumidityList.append(float(data["HUMIDITY"]))
            self.PressureList.append(float(data["PRESSURE"]))
            self.ui.Altitude_Graph.plot(self.XAxisList, self.AltitudeList)
            self.ui.Temperature_Graph.plot(self.XAxisList, self.TempList)
            self.ui.Voltage_Graph.plot(self.XAxisList, self.VoltageList)
            self.ui.Speed_Graph.plot(self.XAxisList, self.SpeedList)
            self.ui.Humidity_Graph.plot(self.XAxisList, self.HumidityList)
            self.ui.Pressure_Graph.plot(self.XAxisList, self.PressureList)

            self.MapPlotPoints.append([float(data["GNSS_LATITUDE"]), float(data["GNSS_LONGITUDE"])])
            self.ThreeDGraphPoints.append([float(data["COMPLIMENTARY_ROLL"]), float(data["COMPLIMENTARY_PITCH"]),
                                           float(data["COMPLIMENTARY_YAW"])])
            self.ThreeDGraphObj.update_orientation(self.ThreeDGraphPoints[-1][0], self.ThreeDGraphPoints[-1][1],
                                                   self.ThreeDGraphPoints[-1][2])

            self.map_threshold_time += 1
            updateMapPoints(self.MapPlotPoints)
            self.UpdateMapWidget()
        except Exception as e:
            print(e)
            print("Error in initial data update.")

    def updateGraph(self, data, x_axis):
        try:
            writeCsv(data.values(), "Flight_050_Data_Files/updateGraph.txt")

            self.XAxisList.append(int(x_axis[-1]) + 1)
            self.AltitudeList.append(float(data["ALTITUDE"]))
            self.TempList.append(float(data["TEMPERATURE"]))
            self.VoltageList.append(float(data["VOLTAGE"]))
            self.SpeedList.append(float(data["VELOCITY"]))
            self.HumidityList.append(float(data["HUMIDITY"]))
            self.PressureList.append(float(data["PRESSURE"]))
            # print(list(map(len, [self.XAxisList, self.AltitudeList, self.TempList, self.VoltageList, self.HumidityList,self.PressureList])))

            self.ui.Altitude_Graph.plot(self.XAxisList, self.AltitudeList)
            self.ui.Temperature_Graph.plot(self.XAxisList, self.TempList)
            self.ui.Voltage_Graph.plot(self.XAxisList, self.VoltageList)
            self.ui.Speed_Graph.plot(self.XAxisList, self.SpeedList)
            self.ui.Humidity_Graph.plot(self.XAxisList, self.HumidityList)
            self.ui.Pressure_Graph.plot(self.XAxisList, self.PressureList)

            self.MapPlotPoints.append([float(data["GNSS_LATITUDE"]), float(data["GNSS_LONGITUDE"])])
            self.ThreeDGraphPoints.append([float(data["COMPLIMENTARY_ROLL"]), float(data["COMPLIMENTARY_PITCH"]),
                                           float(data["COMPLIMENTARY_YAW"])])
            self.ThreeDGraphObj.update_orientation(self.ThreeDGraphPoints[-1][0], self.ThreeDGraphPoints[-1][1],
                                                   self.ThreeDGraphPoints[-1][2])

            self.ui.Altitude_Graph_Text.setText(f"Altitude : {self.AltitudeList[-1]} m")
            self.ui.Temperature_Graph_Text.setText(f"Temperature : {self.TempList[-1]} °C")
            self.ui.Voltage_Graph_Text.setText(f"Voltage : {self.VoltageList[-1]} V")
            self.ui.Speed_Graph_Text.setText(f"Velocity : {self.SpeedList[-1]} m/s")
            self.ui.Humidity_Graph_Text.setText(f"Humidity : {self.HumidityList[-1]} %RH")
            self.ui.Pressure_Graph_Text.setText(f"Pressure : {self.PressureList[-1]} Pa")

            self.map_threshold_time += 1
            if self.map_threshold_time == self.map_threshold:
                self.UpdateMapWidget()
                updateMapPoints(self.MapPlotPoints)
                self.map_threshold_time = 0
        except Exception as e:
            print(e)
            print("Error in graph_update")

    def updateTelemetry(self, data):
        try:
            writeCsv(data.values(), "Flight_050_Data_Files/updateTelemetry.txt")
            self.ui.AccelerometerRoll.setText(f'{data["COMPLIMENTARY_ROLL"]} °')
            self.ui.AccelerometerPitch.setText(f'{data["COMPLIMENTARY_PITCH"]} °')
            self.ui.AccelerometerYaw.setText(f'{data["COMPLIMENTARY_YAW"]} °')

            self.ui.ACCElXPlaceholder.setText(f'{data["ACCEL_X"]} m/s²')
            self.ui.ACCElYPlaceholder.setText(f'{data["ACCEL_Y"]} m/s²')
            self.ui.ACCElZPlaceholder.setText(f'{data["ACCEL_Z"]} m/s²')

            self.ui.AltitutdePlaceholder.setPlainText(f'{data["ALTITUDE"]} m')
            self.ui.TemperaturePlaceholder.setPlainText(f'{data["TEMPERATURE"]} °C')
            self.ui.MissionTimePlaceholder.setPlainText(
                f'{data["GNSS_TIME"]}'
            )
            self.ui.TimePlaceholder.setPlainText(f'{data["TIME"]}')
            self.ui.LatitudePlaceholder.setPlainText(f'{data["GNSS_LATITUDE"]} °')
            self.ui.LongitudePlaceholder.setPlainText(f'{data["GNSS_LONGITUDE"]} °')
            self.ui.GPSAltitudePlaceholder.setPlainText(f'{data["GNSS_ALTITUDE"]} m')
            self.ui.HumidityPlaceholder.setPlainText(f'{data["HUMIDITY"]} %RH')
            self.ui.PressurePlaceholder.setPlainText(f'{data["PRESSURE"]} Pa')

            self.ui.ConnectedStatePlaceholder.setPlainText(
                f'{data["CONNECTED_SATELLITES"]}'
            )
            self.ui.PacketCountPlaceholder.setPlainText(f'{data["PACKET_COUNT"]}')
            self.ui.VoltagePlaceholder.setPlainText(f'{data["VOLTAGE"]} V')
            self.ui.SpeedPlaceholder.setPlainText(f'{data["VELOCITY"]} m/s')
            self.ui.DatePlaceholder.setText(
                f'{datetime.datetime.now().strftime("%m/%d/%Y")}'
            )
            self.progress_calculation = (self.progress_state / self.progress_states) * 100
            if self.ui.ProgressStateDisplay.text() != str(data["STATE"]):
                self.progress_state += 1
            self.progress_calculation = (self.progress_state / self.progress_states) * 100
            self.ui.Gyro1SpinDial.setValue(int(round(float(data["GYRO_1_SPIN_RATE"]), 0)))
            self.ui.Gyro2SpinDial.setValue(int(round(float(data["GYRO_2_SPIN_RATE"]), 0)))
            self.ui.Gyro1SpinDial.setNotchesVisible(True)
            self.ui.Gyro2SpinDial.setNotchesVisible(True)
            self.ui.Gyro1SpinDial.setRange(-9000, 9000)
            self.ui.Gyro2SpinDial.setRange(-9000, 9000)

            self.ui.SpinDial1Placeholder.setText(
                f"Gyro 1 : {data['GYRO_1_SPIN_RATE']} °/s"
            )
            self.ui.SpinDial2Placeholder.setText(
                f"Gyro 2 : {data['GYRO_2_SPIN_RATE']} °/s"
            )

            self.ui.ProgressStateDisplay.setText(data["STATE"])
            self.ui.ProgressStateBar.setValue(int(self.progress_calculation))
            temp_li = ""
            for i in data:
                temp_li += f"{str(data[i])} , "
            temp_li = temp_li[:-2]

            self.ui.TelemetryDummyValues.setText(temp_li)
            self.ui.TelemetryDummyValues.setReadOnly(True)
            self.ui.TelemetryDummyValues.setAlignment(Qt.AlignHCenter)
            self.ui.TelemetryDummyValues.setFontPointSize(10)

            self.ui.GPS_Map_Altitude_Placeholder.setText(f'{data["GNSS_ALTITUDE"]} m')
            updateMapPoints(self.MapPlotPoints)

        except Exception as E:
            print(E)
            print("Error in telemetry update")

    def update_data(self):
        try:
            value_chain = self.ser.readData()
            if value_chain:
                self.updateGraph(value_chain, self.XAxisList)
                self.updateTelemetry(value_chain)
        except Exception as E:
            print(E)
            print("Error in update_data[TelemetryDataUpdate]")


class Communication:
    dummy_Mode = False
    ser = serial.Serial()

    def __init__(self, portname, baudrate=9600):
        self.stateName = "IDLE"
        self.baudrate = baudrate
        self.portname = portname
        if self.portname in ["Dummy Port 1", "Dummy Port 2", "Dummy Port 3"]:
            self.dummyPlug = True
        else:
            self.ser = serial.Serial(self.portname, self.baudrate)
            self.dummyPlug = False

    def write(self, data):
        try:
            print(f"##### Data has been transmitted : {data}")
            self.ser.write(str(data).encode())
        except Exception as e:
            print(e)
            print("----> Error writing command.")

    def readSensorStatus(self):
        if self.dummyPlug:
            return [1] * 6
        while True:
            try:
                value = self.ser.readline().decode("latin1").strip().split(",")
                if len(value) == 4:
                    return value
                else:
                    print("##### Please reset the transmit process.")
                    exit()
            except Exception as e:
                print(f"##### Error reading data from Arduino: {e}")

    def close(self):
        if self.ser.isOpen():
            try:
                self.ser.close()
            except Exception as e:
                print(e)
                print("----> Error closing connection wth connection with xbee.")
        else:
            print("## Connection Already Closed with XBEE.")

    def readData(self):
        try:
            previous_value = readCsv()
            if self.dummyPlug is False:
                value = self.ser.readline().decode("utf-8'").replace("\r", "").replace("\n", "")
                if not value.isprintable():
                    print(f"##### Garbage value detected: {value}")
                    value = previous_value
                value = value.split(",")
                if not value:
                    print("##### Previous value: Transferred")
                    value = previous_value

                STATE_DICT = {
                    0: "Launch Pad",
                    1: "Ascent",
                    2: "Rocket Deploy",
                    3: "Descent",
                    4: "P1 Deployed",
                    5: "Descent Stage 2",
                    6: "P2 Deployed",
                    7: "Touchdown"
                }

                state_id = int(value[20])
                if isinstance(state_id, int):
                    self.stateName = STATE_DICT.get(state_id)
                else:
                    self.stateName = state_id
                if len(value) != 23:
                    value = None
                else:
                    print("#### Value Successfully Passed.")

            else:
                value = None

            value_dict = {
                "ID": value[0] if value else 0,
                "TIME": value[1] if value else 0,
                "PACKET_COUNT": value[2] if value else 0,
                "ALTITUDE": value[3] if value else 0.0,
                "PRESSURE": value[4] if value else 0,
                "TEMPERATURE": value[5] if value else 0.0,
                "VOLTAGE": value[6] if value else 0.00,
                "GNSS_TIME": value[7] if value else 0,
                "GNSS_LONGITUDE": value[8] if value else 72.542049,
                "GNSS_LATITUDE": value[9] if value else 23.129014,
                "GNSS_ALTITUDE": value[10] if value else 0.0,
                "CONNECTED_SATELLITES": value[11] if value else 0,
                "ACCEL_X": value[12] if value else -180,
                "ACCEL_Y": value[13] if value else -180,
                "ACCEL_Z": value[14] if value else -180,
                "COMPLIMENTARY_ROLL": value[15] if value else random.randint(-1, 1),
                "COMPLIMENTARY_PITCH": value[16] if value else random.randint(-1, 1),
                "COMPLIMENTARY_YAW": value[17] if value else random.randint(-1, 1),
                "GYRO_1_SPIN_RATE": value[18] if value else 0,
                "GYRO_2_SPIN_RATE": value[19] if value else 0,
                "STATE": self.stateName if hasattr(self, 'stateName') else "IDLE",
                "HUMIDITY": value[21] if value else 0,
                "VELOCITY": value[22] if value else 0,
            }
            writeCsv(list(value_dict.values()))

            return value_dict

        except Exception as e:
            print(e)
            print("----> Error reading data from xbee.")

    def isDummyMode(self):
        return self.dummyPlug

    def isOpen(self):
        return self.ser.isOpen()


def writeCsv(data, filename="Flight_050_Data_Files/flight_050.csv"):
    try:
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(data)
    except Exception as e:
        print(e)
        print("----> Error Writing data into csv.")


def availablePorts():
    return ["Dummy Port 1", "Dummy Port 2", "Dummy Port 3"]


def backup_html():
    file_path = Path("Flight_050_Data_Files/flight_050.html")
    if not file_path.exists():
        print("File does not exist. Skipping backup.")
        return
    backup_folder = Path("Flight_050_Data_Files/Backup HTMl Files")
    if not backup_folder.exists():
        try:
            backup_folder.mkdir(parents=True)
        except Exception as e:
            print(f"Error making directory {backup_folder}: {e}")
            return

    timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    new_file_name = f"{timestamp}_flight_050.html"
    try:
        with file_path.open("rb") as src_file, (backup_folder / new_file_name).open("wb") as dst_file:
            shutil.copyfileobj(src_file, dst_file)
        file_path.unlink()
        print(f"Backup created: {backup_folder / new_file_name}")
    except Exception as e:
        print(f"Error creating backup: {e}")


def backup_csv():
    file_path = Path("Flight_050_Data_Files/flight_050.csv")
    if not file_path.exists():
        print("File does not exist. Skipping backup.")
        return
    backup_folder = Path("Flight_050_Data_Files/Backup CSV Files")
    if not backup_folder.exists():
        try:
            backup_folder.mkdir(parents=True)
        except Exception as e:
            print(f"Error making directory {backup_folder}: {e}")
            return

    timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    new_file_name = f"{timestamp}_flight_050.csv"
    try:
        with file_path.open("rb") as src_file, (backup_folder / new_file_name).open("wb") as dst_file:
            shutil.copyfileobj(src_file, dst_file)
        file_path.unlink()
        print(f"Backup created: {backup_folder / new_file_name}")
    except Exception as e:
        print(f"Error creating backup: {e}")

    with open("Flight_050_Data_Files/flight_050.csv", "a", newline="") as f:
        fieldnames = [
            "ID",
            "TIME",
            "PACKET COUNT",
            "ALTITUDE",
            "PRESSURE",
            "TEMPERATURE",
            "VOLTAGE",
            "GNSS TIME",
            "GNSS LONGITUDE",
            "GNSS LATITUDE",
            "GNSS ALTITUDE",
            "CONNECTED SATELLITES",
            "ACCEL X",
            "ACCEL Y",
            "ACCEL Z",
            "ROLL",
            "PITCH",
            "YAW",
            "GYRO 1 SPIN RATE",
            "GYRO 2 SPIN RATE",
            "STATE",
            "HUMIDITY",
            "VELOCITY",
        ]
        try:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(fieldnames)
        except Exception as E:
            print(E)
            print("Error writing filenames in csv file")


def readCsv():
    try:
        with open("Flight_050_Data_Files/flight_050.csv", "r", newline="") as f:
            reader = csv.reader(f)
            last_row = None
            for row in reader:
                last_row = row
            if last_row is not None:
                return last_row
    except Exception as e:
        print(e)
        print("----> Error reading data from csv file}.")


def updateMapPoints(points):
    MAP_TILE_URL = "MAPBOX_TILE_URL or OPENMAP_TILE_URL"
    map_data = folium.Map(
        tiles=MAP_TILE_URL,
        zoom_start=19,
        location=points[-1],
        attr=" ",
        max_zoom=100,
    )
    folium.PolyLine(points, color="blue", weight=2.5, opacity=1).add_to(map_data)
    folium.Marker(points[-1], popup="").add_to(map_data)
    folium.Circle(points[-1], radius=5).add_to(map_data)
    map_data.save("Flight_050_Data_Files/flight_050.html")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuiWindow()
    window.show()
    window.showMaximized()
    sys.exit(app.exec_())
