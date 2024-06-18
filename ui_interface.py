from PyQt5.QtCore import QSize, Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QSizePolicy, QWidget, QHBoxLayout, QGridLayout, QLineEdit, QAbstractScrollArea, QTextEdit, \
    QVBoxLayout, \
    QSpacerItem, QGroupBox, QProgressBar, QComboBox, QPushButton, QTabWidget, QFrame, QPlainTextEdit, QDial, QLabel
from pyqtgraph import PlotWidget


class GuiMainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1963, 988)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: #08122C;\n"
                                 "                color:#F0E9D2;\n"
                                 "                font: 9pt \"Segoe UI\";\n"
                                 "            ")
        self.MainWindow_2 = QWidget(MainWindow)
        self.MainWindow_2.setObjectName("MainWindow_2")
        self.horizontalLayout = QHBoxLayout(self.MainWindow_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LogoWidget = QWidget(self.MainWindow_2)
        self.LogoWidget.setObjectName("LogoWidget")
        self.gridLayout_2 = QGridLayout(self.LogoWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 5, 1, 1, 1)
        self.DatePlaceholder = QLineEdit(self.LogoWidget)
        self.DatePlaceholder.setStyleSheet("border-style:outset;\n"
                                           "                                            border-width:2px;\n"
                                           "                                            border-radius: 1px;\n"
                                           "                                            border-color: rgb(0, 199, 179);;\n"
                                           "                                            color:#F0E9D2;\n"
                                           "                                        ")
        self.DatePlaceholder.setAlignment(Qt.AlignCenter)
        self.DatePlaceholder.setReadOnly(True)
        self.DatePlaceholder.setObjectName("DatePlaceholder")
        self.gridLayout_2.addWidget(self.DatePlaceholder, 9, 1, 1, 1)
        self.CansatLogo = QTextEdit(self.LogoWidget)
        self.CansatLogo.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CansatLogo.sizePolicy().hasHeightForWidth())
        self.CansatLogo.setSizePolicy(sizePolicy)
        self.CansatLogo.setMinimumSize(QSize(260, 160))
        self.CansatLogo.setStyleSheet("background-color: #1f232a;")
        self.CansatLogo.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.CansatLogo.setLineWrapMode(QTextEdit.NoWrap)
        self.CansatLogo.setReadOnly(True)
        self.CansatLogo.setObjectName("CansatLogo")
        self.gridLayout_2.addWidget(self.CansatLogo, 4, 1, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)
        self.NameSerialWidget = QWidget(self.LogoWidget)
        self.NameSerialWidget.setMaximumSize(QSize(260, 551))
        self.NameSerialWidget.setStyleSheet("color:rgb(0, 199, 179);;")
        self.NameSerialWidget.setObjectName("NameSerialWidget")
        self.verticalLayout = QVBoxLayout(self.NameSerialWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TeamID = QLineEdit(self.NameSerialWidget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.TeamID.setFont(font)
        self.TeamID.setStyleSheet("border-style:outset;\n"
                                  "                                                        border-width:1px;\n"
                                  "                                                        border-radius: 1px;\n"
                                  "                                                        border-color: rgb(0, 199, 179);;\n"
                                  "                                                        color:#F0E9D2;\n"
                                  "                                                    ")
        self.TeamID.setCursorPosition(21)
        self.TeamID.setAlignment(Qt.AlignCenter)
        self.TeamID.setReadOnly(True)
        self.TeamID.setObjectName("TeamID")
        self.verticalLayout.addWidget(self.TeamID)
        self.TeamName = QLineEdit(self.NameSerialWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TeamName.sizePolicy().hasHeightForWidth())
        self.TeamName.setSizePolicy(sizePolicy)
        self.TeamName.setMaximumSize(QSize(260, 100))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.TeamName.setFont(font)
        self.TeamName.setStyleSheet("border-style:outset;\n"
                                    "                                                        border-width:1px;\n"
                                    "                                                        border-radius: 1px;\n"
                                    "                                                        border-color: rgb(0, 199, 179);;\n"
                                    "                                                        color:#F0E9D2;\n"
                                    "                                                    ")
        self.TeamName.setFrame(True)
        self.TeamName.setAlignment(Qt.AlignCenter)
        self.TeamName.setReadOnly(True)
        self.TeamName.setObjectName("TeamName")
        self.verticalLayout.addWidget(self.TeamName)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.ProgressStateBox = QGroupBox(self.NameSerialWidget)
        self.ProgressStateBox.setStyleSheet("color: white;")
        self.ProgressStateBox.setAlignment(Qt.AlignCenter)
        self.ProgressStateBox.setObjectName("ProgressStateBox")
        self.gridLayout_9 = QGridLayout(self.ProgressStateBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ProgressStateBar = QProgressBar(self.ProgressStateBox)
        self.ProgressStateBar.setStyleSheet("background-color: #08122C;\n"
                                            "                                                                    color:rgb(0, 199, 179);\n"
                                            "                                                                ")
        self.ProgressStateBar.setProperty("value", 12)
        self.ProgressStateBar.setAlignment(Qt.AlignCenter)
        self.ProgressStateBar.setObjectName("ProgressStateBar")
        self.gridLayout_9.addWidget(self.ProgressStateBar, 1, 0, 1, 4)
        self.ProgressStateDisplay = QLineEdit(self.ProgressStateBox)
        self.ProgressStateDisplay.setStyleSheet("background-color: #08122C;\n"
                                                "                                                                    color:rgb(243, 255, 6)\n"
                                                "                                                                ")
        self.ProgressStateDisplay.setText("")
        self.ProgressStateDisplay.setAlignment(Qt.AlignCenter)
        self.ProgressStateDisplay.setReadOnly(True)
        self.ProgressStateDisplay.setObjectName("ProgressStateDisplay")
        self.gridLayout_9.addWidget(self.ProgressStateDisplay, 0, 0, 1, 4)
        self.verticalLayout.addWidget(self.ProgressStateBox)
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.SerialSettings = QLineEdit(self.NameSerialWidget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.SerialSettings.setFont(font)
        self.SerialSettings.setStyleSheet("border-style:outset;\n"
                                          "                                                        border-width:5px;\n"
                                          "                                                        border-radius: 10px;\n"
                                          "                                                        border-color: rgb(0, 199, 179);;\n"
                                          "                                                        color: white;\n"
                                          "                                                    ")
        self.SerialSettings.setAlignment(Qt.AlignCenter)
        self.SerialSettings.setReadOnly(True)
        self.SerialSettings.setObjectName("SerialSettings")
        self.verticalLayout.addWidget(self.SerialSettings)
        self.SerialPort = QLineEdit(self.NameSerialWidget)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.SerialPort.setFont(font)
        self.SerialPort.setStyleSheet("border-width:5px;\n"
                                      "                                                        border-radius: 10px;\n"
                                      "                                                        color: white;\n"
                                      "                                                    ")
        self.SerialPort.setAlignment(Qt.AlignCenter)
        self.SerialPort.setReadOnly(True)
        self.SerialPort.setObjectName("SerialPort")
        self.verticalLayout.addWidget(self.SerialPort, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.PortDropdown = QComboBox(self.NameSerialWidget)
        self.PortDropdown.setStyleSheet("")
        self.PortDropdown.setObjectName("PortDropdown")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.PortDropdown.addItem("")
        self.verticalLayout.addWidget(self.PortDropdown)
        self.BaudRate = QLineEdit(self.NameSerialWidget)
        self.BaudRate.setStyleSheet("border-width:5px;\n"
                                    "                                                        border-radius: 10px;\n"
                                    "                                                        color: white;\n"
                                    "                                                    ")
        self.BaudRate.setAlignment(Qt.AlignCenter)
        self.BaudRate.setReadOnly(True)
        self.BaudRate.setObjectName("BaudRate")
        self.verticalLayout.addWidget(self.BaudRate, 0, Qt.AlignHCenter | Qt.AlignVCenter)
        self.BaudDropdown = QComboBox(self.NameSerialWidget)
        self.BaudDropdown.setStyleSheet("")
        self.BaudDropdown.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.BaudDropdown.setFrame(True)
        self.BaudDropdown.setObjectName("BaudDropdown")
        self.BaudDropdown.addItem("")
        self.BaudDropdown.addItem("")
        self.BaudDropdown.addItem("")
        self.verticalLayout.addWidget(self.BaudDropdown)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.lineEdit = QLineEdit(self.NameSerialWidget)
        self.lineEdit.setStyleSheet("border-width:5px;\n"
                                    "                                                        border-radius: 10px;\n"
                                    "                                                        color: white;\n"
                                    "                                                    ")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.Start = QPushButton(self.NameSerialWidget)
        self.Start.setObjectName("Start")
        self.verticalLayout.addWidget(self.Start)
        self.Calibrate = QPushButton(self.NameSerialWidget)
        self.Calibrate.setObjectName("Calibrate")
        self.verticalLayout.addWidget(self.Calibrate)
        self.gridLayout_2.addWidget(self.NameSerialWidget, 8, 1, 1, 1)
        self.NirmaLogo = QTextEdit(self.LogoWidget)
        self.NirmaLogo.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NirmaLogo.sizePolicy().hasHeightForWidth())
        self.NirmaLogo.setSizePolicy(sizePolicy)
        self.NirmaLogo.setMinimumSize(QSize(240, 115))
        self.NirmaLogo.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.NirmaLogo.setLineWrapMode(QTextEdit.NoWrap)
        self.NirmaLogo.setReadOnly(True)
        self.NirmaLogo.setTabStopDistance(0.0)
        self.NirmaLogo.setCursorWidth(0)
        self.NirmaLogo.setObjectName("NirmaLogo")
        self.gridLayout_2.addWidget(self.NirmaLogo, 3, 1, 1, 1, Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.LogoWidget, 0, Qt.AlignTop)
        self.TabWidget = QWidget(self.MainWindow_2)
        self.TabWidget.setObjectName("TabWidget")
        self.gridLayout = QGridLayout(self.TabWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Tab = QTabWidget(self.TabWidget)
        self.Tab.setAutoFillBackground(False)
        self.Tab.setStyleSheet("background-color: #0F1830;\n"
                               "                                            color: black;\n"
                               "                                            font: 9pt \"Segoe UI\";\n"
                               "                                        ")
        self.Tab.setTabPosition(QTabWidget.North)
        self.Tab.setTabShape(QTabWidget.Rounded)
        self.Tab.setObjectName("Tab")
        self.Data = QWidget()
        self.Data.setObjectName("Data")
        self.TelemetryDummyGroupBox = QGroupBox(self.Data)
        self.TelemetryDummyGroupBox.setGeometry(QRect(20, 0, 1511, 111))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.TelemetryDummyGroupBox.setFont(font)
        self.TelemetryDummyGroupBox.setStyleSheet("color:white;")
        self.TelemetryDummyGroupBox.setAlignment(Qt.AlignCenter)
        self.TelemetryDummyGroupBox.setFlat(False)
        self.TelemetryDummyGroupBox.setCheckable(False)
        self.TelemetryDummyGroupBox.setObjectName("TelemetryDummyGroupBox")
        self.gridLayout_6 = QGridLayout(self.TelemetryDummyGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.TelemetryDummyValues = QTextEdit(self.TelemetryDummyGroupBox)
        self.TelemetryDummyValues.setStyleSheet("background-color: #08122C;\n"
                                                "                                                                color:rgb(0, 199, 179);\n"
                                                "                                                            ")
        self.TelemetryDummyValues.setReadOnly(True)
        self.TelemetryDummyValues.setObjectName("TelemetryDummyValues")
        self.gridLayout_6.addWidget(self.TelemetryDummyValues, 0, 0, 1, 1)
        self.TelemetryDummyRealtimeUpdate = QGroupBox(self.Data)
        self.TelemetryDummyRealtimeUpdate.setGeometry(QRect(20, 110, 1511, 361))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.TelemetryDummyRealtimeUpdate.setFont(font)
        self.TelemetryDummyRealtimeUpdate.setWhatsThis("")
        self.TelemetryDummyRealtimeUpdate.setStyleSheet("color:white;")
        self.TelemetryDummyRealtimeUpdate.setAlignment(Qt.AlignCenter)
        self.TelemetryDummyRealtimeUpdate.setObjectName("TelemetryDummyRealtimeUpdate")
        self.gridLayout_5 = QGridLayout(self.TelemetryDummyRealtimeUpdate)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.TimePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.TimePlaceholder.setReadOnly(True)
        self.TimePlaceholder.setObjectName("TimePlaceholder")
        self.gridLayout_5.addWidget(self.TimePlaceholder, 0, 1, 1, 1)
        self.AltitudeText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.AltitudeText.setFont(font)
        self.AltitudeText.setLayoutDirection(Qt.LeftToRight)
        self.AltitudeText.setStyleSheet("background-color: #08122C;\n"
                                        "                                                                color:rgb(0, 199, 179);\n"
                                        "                                                            ")
        self.AltitudeText.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.AltitudeText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.AltitudeText.setAutoFormatting(QTextEdit.AutoBulletList)
        self.AltitudeText.setDocumentTitle("")
        self.AltitudeText.setUndoRedoEnabled(False)
        self.AltitudeText.setLineWrapMode(QTextEdit.WidgetWidth)
        self.AltitudeText.setReadOnly(True)
        self.AltitudeText.setObjectName("AltitudeText")
        self.gridLayout_5.addWidget(self.AltitudeText, 0, 10, 1, 1)
        self.PacketCountPlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.PacketCountPlaceholder.setReadOnly(True)
        self.PacketCountPlaceholder.setObjectName("PacketCountPlaceholder")
        self.gridLayout_5.addWidget(self.PacketCountPlaceholder, 0, 6, 1, 1)
        self.SpeedText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.SpeedText.setStyleSheet("background-color: #08122C;\n"
                                     "                                                                color:rgb(0, 199, 179);\n"
                                     "                                                            ")
        self.SpeedText.setReadOnly(True)
        self.SpeedText.setObjectName("SpeedText")
        self.gridLayout_5.addWidget(self.SpeedText, 4, 10, 1, 1)
        self.LongitudePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.LongitudePlaceholder.setReadOnly(True)
        self.LongitudePlaceholder.setObjectName("LongitudePlaceholder")
        self.gridLayout_5.addWidget(self.LongitudePlaceholder, 2, 12, 1, 1)
        self.SpeedPlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.SpeedPlaceholder.setReadOnly(True)
        self.SpeedPlaceholder.setObjectName("SpeedPlaceholder")
        self.gridLayout_5.addWidget(self.SpeedPlaceholder, 4, 12, 1, 1)
        self.HumidityText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.HumidityText.setStyleSheet("background-color: #08122C;\n"
                                        "                                                                color:rgb(0, 199, 179);\n"
                                        "                                                            ")
        self.HumidityText.setReadOnly(True)
        self.HumidityText.setObjectName("HumidityText")
        self.gridLayout_5.addWidget(self.HumidityText, 6, 4, 1, 1)
        self.LineSplit2 = QFrame(self.TelemetryDummyRealtimeUpdate)
        self.LineSplit2.setFrameShape(QFrame.VLine)
        self.LineSplit2.setFrameShadow(QFrame.Sunken)
        self.LineSplit2.setObjectName("LineSplit2")
        self.gridLayout_5.addWidget(self.LineSplit2, 0, 3, 7, 1)
        self.TemperaturePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.TemperaturePlaceholder.setReadOnly(True)
        self.TemperaturePlaceholder.setObjectName("TemperaturePlaceholder")
        self.gridLayout_5.addWidget(self.TemperaturePlaceholder, 1, 6, 1, 1)
        self.MissionTimeText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.MissionTimeText.setStyleSheet("background-color: #08122C;\n"
                                           "                                                                color:rgb(0, 199, 179);\n"
                                           "                                                            ")
        self.MissionTimeText.setReadOnly(True)
        self.MissionTimeText.setObjectName("MissionTimeText")
        self.gridLayout_5.addWidget(self.MissionTimeText, 2, 0, 1, 1)
        self.LineSplit4 = QFrame(self.TelemetryDummyRealtimeUpdate)
        self.LineSplit4.setFrameShape(QFrame.VLine)
        self.LineSplit4.setFrameShadow(QFrame.Sunken)
        self.LineSplit4.setObjectName("LineSplit4")
        self.gridLayout_5.addWidget(self.LineSplit4, 0, 9, 7, 1)
        self.PressurePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.PressurePlaceholder.setReadOnly(True)
        self.PressurePlaceholder.setObjectName("PressurePlaceholder")
        self.gridLayout_5.addWidget(self.PressurePlaceholder, 1, 1, 1, 1)
        self.LatitiudeText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.LatitiudeText.setStyleSheet("background-color: #08122C;\n"
                                         "                                                                color:rgb(0, 199, 179);\n"
                                         "                                                            ")
        self.LatitiudeText.setReadOnly(True)
        self.LatitiudeText.setObjectName("LatitiudeText")
        self.gridLayout_5.addWidget(self.LatitiudeText, 2, 4, 1, 1)
        self.VoltagePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.VoltagePlaceholder.setReadOnly(True)
        self.VoltagePlaceholder.setObjectName("VoltagePlaceholder")
        self.gridLayout_5.addWidget(self.VoltagePlaceholder, 1, 12, 1, 1)
        self.LineSplit1 = QFrame(self.TelemetryDummyRealtimeUpdate)
        self.LineSplit1.setFrameShape(QFrame.VLine)
        self.LineSplit1.setFrameShadow(QFrame.Sunken)
        self.LineSplit1.setObjectName("LineSplit1")
        self.gridLayout_5.addWidget(self.LineSplit1, 0, 2, 7, 1)
        self.LongitudeText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.LongitudeText.setStyleSheet("background-color: #08122C;\n"
                                         "                                                                color:rgb(0, 199, 179);\n"
                                         "                                                            ")
        self.LongitudeText.setReadOnly(True)
        self.LongitudeText.setObjectName("LongitudeText")
        self.gridLayout_5.addWidget(self.LongitudeText, 2, 10, 1, 1)
        self.AltitutdePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.AltitutdePlaceholder.setReadOnly(True)
        self.AltitutdePlaceholder.setObjectName("AltitutdePlaceholder")
        self.gridLayout_5.addWidget(self.AltitutdePlaceholder, 0, 12, 1, 1)
        self.HumidityPlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.HumidityPlaceholder.setFont(font)
        self.HumidityPlaceholder.setReadOnly(True)
        self.HumidityPlaceholder.setObjectName("HumidityPlaceholder")
        self.gridLayout_5.addWidget(self.HumidityPlaceholder, 6, 6, 1, 1)
        self.ConnectedStatePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.ConnectedStatePlaceholder.setReadOnly(True)
        self.ConnectedStatePlaceholder.setObjectName("ConnectedStatePlaceholder")
        self.gridLayout_5.addWidget(self.ConnectedStatePlaceholder, 4, 6, 1, 1)
        self.GPSAltitudePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.GPSAltitudePlaceholder.setReadOnly(True)
        self.GPSAltitudePlaceholder.setObjectName("GPSAltitudePlaceholder")
        self.gridLayout_5.addWidget(self.GPSAltitudePlaceholder, 4, 1, 1, 1)
        self.TimeText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.TimeText.setFont(font)
        self.TimeText.setLayoutDirection(Qt.LeftToRight)
        self.TimeText.setStyleSheet("background-color: #08122C;\n"
                                    "                                                                color:rgb(0, 199, 179);\n"
                                    "                                                            ")
        self.TimeText.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.TimeText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.TimeText.setAutoFormatting(QTextEdit.AutoBulletList)
        self.TimeText.setDocumentTitle("")
        self.TimeText.setUndoRedoEnabled(False)
        self.TimeText.setLineWrapMode(QTextEdit.WidgetWidth)
        self.TimeText.setReadOnly(True)
        self.TimeText.setObjectName("TimeText")
        self.gridLayout_5.addWidget(self.TimeText, 0, 0, 1, 1)
        self.PacketCountText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.PacketCountText.setStyleSheet("background-color: #08122C;\n"
                                           "                                                                color:rgb(0, 199, 179);\n"
                                           "                                                            ")
        self.PacketCountText.setReadOnly(True)
        self.PacketCountText.setObjectName("PacketCountText")
        self.gridLayout_5.addWidget(self.PacketCountText, 0, 4, 1, 1)
        self.LatitudePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.LatitudePlaceholder.setReadOnly(True)
        self.LatitudePlaceholder.setObjectName("LatitudePlaceholder")
        self.gridLayout_5.addWidget(self.LatitudePlaceholder, 2, 6, 1, 1)
        self.LineSplit3 = QFrame(self.TelemetryDummyRealtimeUpdate)
        self.LineSplit3.setFrameShape(QFrame.VLine)
        self.LineSplit3.setFrameShadow(QFrame.Sunken)
        self.LineSplit3.setObjectName("LineSplit3")
        self.gridLayout_5.addWidget(self.LineSplit3, 0, 8, 7, 1)
        self.MissionTimePlaceholder = QPlainTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.MissionTimePlaceholder.setReadOnly(True)
        self.MissionTimePlaceholder.setObjectName("MissionTimePlaceholder")
        self.gridLayout_5.addWidget(self.MissionTimePlaceholder, 2, 1, 1, 1)
        self.VoltageText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.VoltageText.setStyleSheet("background-color: #08122C;\n"
                                       "                                                                color:rgb(0, 199, 179);\n"
                                       "                                                            ")
        self.VoltageText.setReadOnly(True)
        self.VoltageText.setObjectName("VoltageText")
        self.gridLayout_5.addWidget(self.VoltageText, 1, 10, 1, 1)
        self.TemperatureText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.TemperatureText.setStyleSheet("background-color: #08122C;\n"
                                           "                                                                color:rgb(0, 199, 179);\n"
                                           "                                                            ")
        self.TemperatureText.setReadOnly(True)
        self.TemperatureText.setObjectName("TemperatureText")
        self.gridLayout_5.addWidget(self.TemperatureText, 1, 4, 1, 1)
        self.PressureText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.PressureText.setStyleSheet("background-color: #08122C;\n"
                                        "                                                                color:rgb(0, 199, 179);\n"
                                        "                                                            ")
        self.PressureText.setReadOnly(True)
        self.PressureText.setObjectName("PressureText")
        self.gridLayout_5.addWidget(self.PressureText, 1, 0, 1, 1)
        self.GPSAltitudeText = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.GPSAltitudeText.setStyleSheet("background-color: #08122C;\n"
                                           "                                                                color:rgb(0, 199, 179);\n"
                                           "                                                            ")
        self.GPSAltitudeText.setReadOnly(True)
        self.GPSAltitudeText.setObjectName("GPSAltitudeText")
        self.gridLayout_5.addWidget(self.GPSAltitudeText, 4, 0, 1, 1)
        self.LatitiudeText_2 = QTextEdit(self.TelemetryDummyRealtimeUpdate)
        self.LatitiudeText_2.setStyleSheet("background-color: #08122C;\n"
                                           "                                                                color:rgb(0, 199, 179);\n"
                                           "                                                            ")
        self.LatitiudeText_2.setReadOnly(True)
        self.LatitiudeText_2.setObjectName("LatitiudeText_2")
        self.gridLayout_5.addWidget(self.LatitiudeText_2, 4, 4, 1, 1)
        self.ThreeDDataGroupBox = QGroupBox(self.Data)
        self.ThreeDDataGroupBox.setGeometry(QRect(260, 480, 321, 221))
        self.ThreeDDataGroupBox.setStyleSheet("color:white")
        self.ThreeDDataGroupBox.setAlignment(Qt.AlignCenter)
        self.ThreeDDataGroupBox.setObjectName("ThreeDDataGroupBox")
        self.gridLayout_7 = QGridLayout(self.ThreeDDataGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Roll = QLineEdit(self.ThreeDDataGroupBox)
        self.Roll.setStyleSheet("background-color: #08122C;\n"
                                "                                                                color:rgb(0, 199, 179);\n"
                                "                                                            ")
        self.Roll.setAlignment(Qt.AlignCenter)
        self.Roll.setReadOnly(True)
        self.Roll.setObjectName("Roll")
        self.gridLayout_7.addWidget(self.Roll, 1, 1, 1, 2)
        self.AccelerometerYaw = QLabel(self.ThreeDDataGroupBox)
        self.AccelerometerYaw.setFrameShape(QFrame.Box)
        self.AccelerometerYaw.setAlignment(Qt.AlignCenter)
        self.AccelerometerYaw.setObjectName("AccelerometerYaw")
        self.gridLayout_7.addWidget(self.AccelerometerYaw, 4, 3, 1, 2)
        self.AccelerometerPitch = QLabel(self.ThreeDDataGroupBox)
        self.AccelerometerPitch.setFrameShape(QFrame.Box)
        self.AccelerometerPitch.setAlignment(Qt.AlignCenter)
        self.AccelerometerPitch.setObjectName("AccelerometerPitch")
        self.gridLayout_7.addWidget(self.AccelerometerPitch, 3, 3, 1, 2)
        self.Pitch = QLineEdit(self.ThreeDDataGroupBox)
        self.Pitch.setStyleSheet("background-color: #08122C;\n"
                                 "                                                                color:rgb(0, 199, 179);\n"
                                 "                                                            ")
        self.Pitch.setAlignment(Qt.AlignCenter)
        self.Pitch.setReadOnly(True)
        self.Pitch.setObjectName("Pitch")
        self.gridLayout_7.addWidget(self.Pitch, 3, 1, 1, 2)
        self.Yaw = QLineEdit(self.ThreeDDataGroupBox)
        self.Yaw.setStyleSheet("background-color: #08122C;\n"
                               "                                                                color:rgb(0, 199, 179);\n"
                               "                                                            ")
        self.Yaw.setAlignment(Qt.AlignCenter)
        self.Yaw.setReadOnly(True)
        self.Yaw.setObjectName("Yaw")
        self.gridLayout_7.addWidget(self.Yaw, 4, 1, 1, 2)
        self.AccelerometerRoll = QLabel(self.ThreeDDataGroupBox)
        self.AccelerometerRoll.setFrameShape(QFrame.Box)
        self.AccelerometerRoll.setAlignment(Qt.AlignCenter)
        self.AccelerometerRoll.setObjectName("AccelerometerRoll")
        self.gridLayout_7.addWidget(self.AccelerometerRoll, 1, 3, 1, 2)
        self.ThreeDGraph = QGroupBox(self.Data)
        self.ThreeDGraph.setGeometry(QRect(590, 490, 451, 401))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThreeDGraph.sizePolicy().hasHeightForWidth())
        self.ThreeDGraph.setSizePolicy(sizePolicy)
        self.ThreeDGraph.setStyleSheet("background-color: #08122C;\n"
                                       "                                                    color:white;\n"
                                       "                                                ")
        self.ThreeDGraph.setTitle("")
        self.ThreeDGraph.setAlignment(Qt.AlignCenter)
        self.ThreeDGraph.setObjectName("ThreeDGraph")
        self.gridLayout_8 = QGridLayout(self.ThreeDGraph)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_2 = QLineEdit(self.ThreeDGraph)
        self.lineEdit_2.setStyleSheet("background-color: #08122C;\n"
                                      "                                                                color:rgb(0, 199, 179);\n"
                                      "                                                            ")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_8.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.ThreeDGraphWidget = QWidget(self.ThreeDGraph)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThreeDGraphWidget.sizePolicy().hasHeightForWidth())
        self.ThreeDGraphWidget.setSizePolicy(sizePolicy)
        self.ThreeDGraphWidget.setLayoutDirection(Qt.LeftToRight)
        self.ThreeDGraphWidget.setObjectName("ThreeDGraphWidget")
        self.gridLayout_8.addWidget(self.ThreeDGraphWidget, 0, 0, 1, 1)
        self.ACCELFrame = QFrame(self.Data)
        self.ACCELFrame.setGeometry(QRect(260, 760, 321, 131))
        self.ACCELFrame.setStyleSheet("color:white;\n"
                                      "                                                    border-width:3px;\n"
                                      "                                                ")
        self.ACCELFrame.setFrameShape(QFrame.Box)
        self.ACCELFrame.setFrameShadow(QFrame.Sunken)
        self.ACCELFrame.setLineWidth(0)
        self.ACCELFrame.setMidLineWidth(1)
        self.ACCELFrame.setObjectName("ACCELFrame")
        self.gridLayout_10 = QGridLayout(self.ACCELFrame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.Magnetometer_2 = QLineEdit(self.ACCELFrame)
        self.Magnetometer_2.setStyleSheet("border-style:offset;")
        self.Magnetometer_2.setText("")
        self.Magnetometer_2.setAlignment(Qt.AlignCenter)
        self.Magnetometer_2.setReadOnly(True)
        self.Magnetometer_2.setObjectName("Magnetometer_2")
        self.gridLayout_10.addWidget(self.Magnetometer_2, 0, 0, 1, 1, Qt.AlignLeft)
        self.MagenetometerRoll_2 = QLabel(self.ACCELFrame)
        self.MagenetometerRoll_2.setStyleSheet("background-color: #08122C;\n"
                                               "                                                                color:rgb(0, 199, 179);\n"
                                               "                                                            ")
        self.MagenetometerRoll_2.setFrameShape(QFrame.Box)
        self.MagenetometerRoll_2.setAlignment(Qt.AlignCenter)
        self.MagenetometerRoll_2.setObjectName("MagenetometerRoll_2")
        self.gridLayout_10.addWidget(self.MagenetometerRoll_2, 0, 1, 1, 1)
        self.MagenetometerRoll_3 = QLabel(self.ACCELFrame)
        self.MagenetometerRoll_3.setStyleSheet("background-color: #08122C;\n"
                                               "                                                                color:rgb(0, 199, 179);\n"
                                               "                                                            ")
        self.MagenetometerRoll_3.setFrameShape(QFrame.Box)
        self.MagenetometerRoll_3.setAlignment(Qt.AlignCenter)
        self.MagenetometerRoll_3.setObjectName("MagenetometerRoll_3")
        self.gridLayout_10.addWidget(self.MagenetometerRoll_3, 0, 2, 1, 1)
        self.MagenetometerRoll_4 = QLabel(self.ACCELFrame)
        self.MagenetometerRoll_4.setStyleSheet("background-color: #08122C;\n"
                                               "                                                                color:rgb(0, 199, 179);\n"
                                               "                                                            ")
        self.MagenetometerRoll_4.setFrameShape(QFrame.Box)
        self.MagenetometerRoll_4.setAlignment(Qt.AlignCenter)
        self.MagenetometerRoll_4.setObjectName("MagenetometerRoll_4")
        self.gridLayout_10.addWidget(self.MagenetometerRoll_4, 0, 3, 1, 1)
        self.ACCElText = QLineEdit(self.ACCELFrame)
        self.ACCElText.setStyleSheet("background-color: #08122C;\n"
                                     "                                                                color:rgb(0, 199, 179);\n"
                                     "                                                            ")
        self.ACCElText.setAlignment(Qt.AlignCenter)
        self.ACCElText.setReadOnly(True)
        self.ACCElText.setObjectName("ACCElText")
        self.gridLayout_10.addWidget(self.ACCElText, 1, 0, 1, 1, Qt.AlignLeft)
        self.ACCElXPlaceholder = QLabel(self.ACCELFrame)
        self.ACCElXPlaceholder.setFrameShape(QFrame.Box)
        self.ACCElXPlaceholder.setAlignment(Qt.AlignCenter)
        self.ACCElXPlaceholder.setObjectName("ACCElXPlaceholder")
        self.gridLayout_10.addWidget(self.ACCElXPlaceholder, 1, 1, 1, 1)
        self.ACCElYPlaceholder = QLabel(self.ACCELFrame)
        self.ACCElYPlaceholder.setFrameShape(QFrame.Box)
        self.ACCElYPlaceholder.setAlignment(Qt.AlignCenter)
        self.ACCElYPlaceholder.setObjectName("ACCElYPlaceholder")
        self.gridLayout_10.addWidget(self.ACCElYPlaceholder, 1, 2, 1, 1)
        self.ACCElZPlaceholder = QLabel(self.ACCELFrame)
        self.ACCElZPlaceholder.setFrameShape(QFrame.Box)
        self.ACCElZPlaceholder.setAlignment(Qt.AlignCenter)
        self.ACCElZPlaceholder.setObjectName("ACCElZPlaceholder")
        self.gridLayout_10.addWidget(self.ACCElZPlaceholder, 1, 3, 1, 1)
        self.groupBox = QGroupBox(self.Data)
        self.groupBox.setGeometry(QRect(1050, 490, 481, 401))
        self.groupBox.setStyleSheet("background-color: #08122C;\n"
                                    "                                                    color:white;\n"
                                    "                                                ")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_11 = QGridLayout(self.groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.Gyro1SpinDial = QDial(self.groupBox)
        self.Gyro1SpinDial.setObjectName("Gyro1SpinDial")
        self.gridLayout_11.addWidget(self.Gyro1SpinDial, 0, 0, 2, 1)
        self.Gyro2SpinDial = QDial(self.groupBox)
        self.Gyro2SpinDial.setObjectName("Gyro2SpinDial")
        self.gridLayout_11.addWidget(self.Gyro2SpinDial, 0, 2, 2, 1)
        self.SpinDial1Placeholder = QLineEdit(self.groupBox)
        self.SpinDial1Placeholder.setStyleSheet("background-color: #08122C;\n"
                                                "                                                                color:rgb(0, 199, 179);\n"
                                                "                                                            ")
        self.SpinDial1Placeholder.setAlignment(Qt.AlignCenter)
        self.SpinDial1Placeholder.setReadOnly(True)
        self.SpinDial1Placeholder.setObjectName("SpinDial1Placeholder")
        self.gridLayout_11.addWidget(self.SpinDial1Placeholder, 2, 0, 1, 1)
        self.SpinDial2Placeholder = QLineEdit(self.groupBox)
        self.SpinDial2Placeholder.setStyleSheet("background-color: #08122C;\n"
                                                "                                                                color:rgb(0, 199, 179);\n"
                                                "                                                                border-color:rgb(0, 199, 179);\n"
                                                "                                                            ")
        self.SpinDial2Placeholder.setAlignment(Qt.AlignCenter)
        self.SpinDial2Placeholder.setReadOnly(True)
        self.SpinDial2Placeholder.setObjectName("SpinDial2Placeholder")
        self.gridLayout_11.addWidget(self.SpinDial2Placeholder, 2, 2, 1, 1)
        self.SensorStatus = QGroupBox(self.Data)
        self.SensorStatus.setGeometry(QRect(20, 480, 231, 411))
        self.SensorStatus.setStyleSheet("color:white")
        self.SensorStatus.setAlignment(Qt.AlignCenter)
        self.SensorStatus.setObjectName("SensorStatus")
        self.gridLayout_12 = QGridLayout(self.SensorStatus)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.Reset_Label = QLineEdit(self.SensorStatus)
        self.Reset_Label.setStyleSheet("background-color: #08122C;\n"
                                       "                                                                color:rgb(0, 199, 179);\n"
                                       "                                                            ")
        self.Reset_Label.setAlignment(Qt.AlignCenter)
        self.Reset_Label.setReadOnly(True)
        self.Reset_Label.setObjectName("Reset_Label")
        self.gridLayout_12.addWidget(self.Reset_Label, 6, 1, 1, 1)
        self.IMU_TEXT = QLabel(self.SensorStatus)
        self.IMU_TEXT.setFrameShape(QFrame.Box)
        self.IMU_TEXT.setAlignment(Qt.AlignCenter)
        self.IMU_TEXT.setObjectName("IMU_TEXT")
        self.gridLayout_12.addWidget(self.IMU_TEXT, 3, 3, 1, 2)
        self.Pressure_Label = QLineEdit(self.SensorStatus)
        self.Pressure_Label.setStyleSheet("background-color: #08122C;\n"
                                          "color:rgb(0, 199, 179);\n"
                                          "                                                            ")
        self.Pressure_Label.setAlignment(Qt.AlignCenter)
        self.Pressure_Label.setReadOnly(True)
        self.Pressure_Label.setObjectName("Pressure_Label")
        self.gridLayout_12.addWidget(self.Pressure_Label, 4, 1, 1, 1)
        self.TEMP_TEXT = QLabel(self.SensorStatus)
        self.TEMP_TEXT.setFrameShape(QFrame.Box)
        self.TEMP_TEXT.setAlignment(Qt.AlignCenter)
        self.TEMP_TEXT.setObjectName("TEMP_TEXT")
        self.gridLayout_12.addWidget(self.TEMP_TEXT, 5, 3, 1, 2)
        self.RTC_Label = QLineEdit(self.SensorStatus)
        self.RTC_Label.setStyleSheet("background-color: #08122C;\n"
                                     "                                                                color:rgb(0, 199, 179);\n"
                                     "                                                            ")
        self.RTC_Label.setAlignment(Qt.AlignCenter)
        self.RTC_Label.setReadOnly(True)
        self.RTC_Label.setObjectName("RTC_Label")
        self.gridLayout_12.addWidget(self.RTC_Label, 1, 1, 1, 1)
        self.RTC_TEXT = QLabel(self.SensorStatus)
        self.RTC_TEXT.setFrameShape(QFrame.Box)
        self.RTC_TEXT.setAlignment(Qt.AlignCenter)
        self.RTC_TEXT.setObjectName("RTC_TEXT")
        self.gridLayout_12.addWidget(self.RTC_TEXT, 1, 3, 1, 2)
        self.IMU_Label = QLineEdit(self.SensorStatus)
        self.IMU_Label.setStyleSheet("background-color: #08122C;\n"
                                     "                                                                color:rgb(0, 199, 179);\n"
                                     "                                                            ")
        self.IMU_Label.setAlignment(Qt.AlignCenter)
        self.IMU_Label.setReadOnly(True)
        self.IMU_Label.setObjectName("IMU_Label")
        self.gridLayout_12.addWidget(self.IMU_Label, 3, 1, 1, 1)
        self.RESET_TEXT = QLabel(self.SensorStatus)
        self.RESET_TEXT.setFrameShape(QFrame.Box)
        self.RESET_TEXT.setAlignment(Qt.AlignCenter)
        self.RESET_TEXT.setObjectName("RESET_TEXT")
        self.gridLayout_12.addWidget(self.RESET_TEXT, 6, 3, 1, 2)
        self.PRESSURE_TEXT = QLabel(self.SensorStatus)
        self.PRESSURE_TEXT.setFrameShape(QFrame.Box)
        self.PRESSURE_TEXT.setAlignment(Qt.AlignCenter)
        self.PRESSURE_TEXT.setObjectName("PRESSURE_TEXT")
        self.gridLayout_12.addWidget(self.PRESSURE_TEXT, 4, 3, 1, 2)
        self.Temp_Label = QLineEdit(self.SensorStatus)
        self.Temp_Label.setStyleSheet("background-color: #08122C;\n"
                                      "                                                                color:rgb(0, 199, 179);\n"
                                      "                                                            ")
        self.Temp_Label.setAlignment(Qt.AlignCenter)
        self.Temp_Label.setReadOnly(True)
        self.Temp_Label.setObjectName("Temp_Label")
        self.gridLayout_12.addWidget(self.Temp_Label, 5, 1, 1, 1)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/QSS/icons/database.png"), QIcon.Normal, QIcon.Off)
        self.Tab.addTab(self.Data, icon1, "")
        self.Graph = QWidget()
        self.Graph.setObjectName("Graph")
        self.gridLayout_13 = QGridLayout(self.Graph)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.Humidity_Graph_Text = QLineEdit(self.Graph)
        self.Humidity_Graph_Text.setStyleSheet("background-color: #08122C;\n"
                                               "                                                            color:rgb(0, 199, 179);\n"
                                               "                                                        ")
        self.Humidity_Graph_Text.setAlignment(Qt.AlignCenter)
        self.Humidity_Graph_Text.setDragEnabled(False)
        self.Humidity_Graph_Text.setReadOnly(True)
        self.Humidity_Graph_Text.setObjectName("Humidity_Graph_Text")
        self.gridLayout_13.addWidget(self.Humidity_Graph_Text, 6, 3, 1, 1)
        spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem4, 1, 4, 6, 1)
        spacerItem5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem5, 0, 0, 8, 1)
        self.Voltage_Graph = PlotWidget(self.Graph)
        self.Voltage_Graph.setObjectName("Voltage_Graph")
        self.gridLayout_13.addWidget(self.Voltage_Graph, 1, 3, 1, 1)
        spacerItem6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem6, 7, 1, 1, 4)
        self.Speed_Graph_Text = QLineEdit(self.Graph)
        self.Speed_Graph_Text.setStyleSheet("background-color: #08122C;\n"
                                            "                                                            color:rgb(0, 199, 179);\n"
                                            "                                                        ")
        self.Speed_Graph_Text.setAlignment(Qt.AlignCenter)
        self.Speed_Graph_Text.setDragEnabled(False)
        self.Speed_Graph_Text.setReadOnly(True)
        self.Speed_Graph_Text.setObjectName("Speed_Graph_Text")
        self.gridLayout_13.addWidget(self.Speed_Graph_Text, 6, 2, 1, 1)
        self.Temperature_Graph_Text = QLineEdit(self.Graph)
        self.Temperature_Graph_Text.setStyleSheet("background-color: #08122C;\n"
                                                  "                                                            color:rgb(0, 199, 179);\n"
                                                  "                                                        ")
        self.Temperature_Graph_Text.setAlignment(Qt.AlignCenter)
        self.Temperature_Graph_Text.setDragEnabled(False)
        self.Temperature_Graph_Text.setReadOnly(True)
        self.Temperature_Graph_Text.setObjectName("Temperature_Graph_Text")
        self.gridLayout_13.addWidget(self.Temperature_Graph_Text, 2, 2, 1, 1)
        self.Pressure_Graph_Text = QLineEdit(self.Graph)
        self.Pressure_Graph_Text.setStyleSheet("background-color: #08122C;\n"
                                               "                                                            color:rgb(0, 199, 179);\n"
                                               "                                                        ")
        self.Pressure_Graph_Text.setAlignment(Qt.AlignCenter)
        self.Pressure_Graph_Text.setDragEnabled(False)
        self.Pressure_Graph_Text.setReadOnly(True)
        self.Pressure_Graph_Text.setObjectName("Pressure_Graph_Text")
        self.gridLayout_13.addWidget(self.Pressure_Graph_Text, 6, 1, 1, 1)
        self.Altitude_Graph = PlotWidget(self.Graph)
        self.Altitude_Graph.setObjectName("Altitude_Graph")
        self.gridLayout_13.addWidget(self.Altitude_Graph, 1, 1, 1, 1)
        self.Altitude_Graph_Text = QLineEdit(self.Graph)
        self.Altitude_Graph_Text.setStyleSheet("background-color: #08122C;\n"
                                               "                                                            color:rgb(0, 199, 179);\n"
                                               "                                                        ")
        self.Altitude_Graph_Text.setAlignment(Qt.AlignCenter)
        self.Altitude_Graph_Text.setDragEnabled(False)
        self.Altitude_Graph_Text.setReadOnly(True)
        self.Altitude_Graph_Text.setObjectName("Altitude_Graph_Text")
        self.gridLayout_13.addWidget(self.Altitude_Graph_Text, 2, 1, 1, 1)
        self.Pressure_Graph = PlotWidget(self.Graph)
        self.Pressure_Graph.setObjectName("Pressure_Graph")
        self.gridLayout_13.addWidget(self.Pressure_Graph, 5, 1, 1, 1)
        spacerItem7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem7, 0, 1, 1, 4)
        self.Speed_Graph = PlotWidget(self.Graph)
        self.Speed_Graph.setObjectName("Speed_Graph")
        self.gridLayout_13.addWidget(self.Speed_Graph, 5, 2, 1, 1)
        self.Voltage_Graph_Text = QLineEdit(self.Graph)
        self.Voltage_Graph_Text.setStyleSheet("background-color: #08122C;\n"
                                              "                                                            color:rgb(0, 199, 179);\n"
                                              "                                                        ")
        self.Voltage_Graph_Text.setAlignment(Qt.AlignCenter)
        self.Voltage_Graph_Text.setDragEnabled(False)
        self.Voltage_Graph_Text.setReadOnly(True)
        self.Voltage_Graph_Text.setObjectName("Voltage_Graph_Text")
        self.gridLayout_13.addWidget(self.Voltage_Graph_Text, 2, 3, 1, 1)
        self.Temperature_Graph = PlotWidget(self.Graph)
        self.Temperature_Graph.setObjectName("Temperature_Graph")
        self.gridLayout_13.addWidget(self.Temperature_Graph, 1, 2, 1, 1)
        spacerItem8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem8, 4, 1, 1, 3)
        self.Humidity_Graph = PlotWidget(self.Graph)
        self.Humidity_Graph.setObjectName("Humidity_Graph")
        self.gridLayout_13.addWidget(self.Humidity_Graph, 5, 3, 1, 1)
        spacerItem9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem9, 3, 1, 1, 3)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/QSS/icons/activity.png"), QIcon.Normal, QIcon.Off)
        self.Tab.addTab(self.Graph, icon2, "")
        self.Map = QWidget()
        self.Map.setObjectName("Map")
        self.gridLayout_3 = QGridLayout(self.Map)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MapCombinedFrame = QFrame(self.Map)
        self.MapCombinedFrame.setFrameShape(QFrame.StyledPanel)
        self.MapCombinedFrame.setFrameShadow(QFrame.Raised)
        self.MapCombinedFrame.setObjectName("MapCombinedFrame")
        self.gridLayout_4 = QGridLayout(self.MapCombinedFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LatFrame = QFrame(self.MapCombinedFrame)
        self.LatFrame.setStyleSheet("color:rgb(0, 199, 179);;\n"
                                    "                                                                    ")
        self.LatFrame.setFrameShape(QFrame.StyledPanel)
        self.LatFrame.setFrameShadow(QFrame.Raised)
        self.LatFrame.setObjectName("LatFrame")
        self.horizontalLayout_2 = QHBoxLayout(self.LatFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.Latitude = QLineEdit(self.LatFrame)
        self.Latitude.setStyleSheet("background-color:\n"
                                    "                                                                                    #08122C;\n"
                                    "                                                                                    color:rgb(0, 199, 179);\n"
                                    "                                                                                ")
        self.Latitude.setAlignment(Qt.AlignCenter)
        self.Latitude.setReadOnly(True)
        self.Latitude.setObjectName("Latitude")
        self.horizontalLayout_2.addWidget(self.Latitude)
        self.Lat_Text = QLineEdit(self.LatFrame)
        self.Lat_Text.setAlignment(Qt.AlignCenter)
        self.Lat_Text.setReadOnly(True)
        self.Lat_Text.setObjectName("Lat_Text")
        self.horizontalLayout_2.addWidget(self.Lat_Text)
        spacerItem11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.Longitude = QLineEdit(self.LatFrame)
        self.Longitude.setStyleSheet("background-color:\n"
                                     "                                                                                    #08122C;\n"
                                     "                                                                                    color:rgb(0, 199, 179);\n"
                                     "                                                                                ")
        self.Longitude.setAlignment(Qt.AlignCenter)
        self.Longitude.setReadOnly(True)
        self.Longitude.setObjectName("Longitude")
        self.horizontalLayout_2.addWidget(self.Longitude)
        self.Longi_Text = QLineEdit(self.LatFrame)
        self.Longi_Text.setAlignment(Qt.AlignCenter)
        self.Longi_Text.setReadOnly(True)
        self.Longi_Text.setObjectName("Longi_Text")
        self.horizontalLayout_2.addWidget(self.Longi_Text)
        spacerItem12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.GPS_Map_Altitude_Text = QLineEdit(self.LatFrame)
        self.GPS_Map_Altitude_Text.setStyleSheet("background-color:\n"
                                                 "                                                                                    #08122C;\n"
                                                 "                                                                                    color:rgb(0, 199, 179);\n"
                                                 "                                                                                ")
        self.GPS_Map_Altitude_Text.setAlignment(Qt.AlignCenter)
        self.GPS_Map_Altitude_Text.setReadOnly(True)
        self.GPS_Map_Altitude_Text.setObjectName("GPS_Map_Altitude_Text")
        self.horizontalLayout_2.addWidget(self.GPS_Map_Altitude_Text)
        self.GPS_Map_Altitude_Placeholder = QLineEdit(self.LatFrame)
        self.GPS_Map_Altitude_Placeholder.setAlignment(Qt.AlignCenter)
        self.GPS_Map_Altitude_Placeholder.setReadOnly(True)
        self.GPS_Map_Altitude_Placeholder.setObjectName("GPS_Map_Altitude_Placeholder")
        self.horizontalLayout_2.addWidget(self.GPS_Map_Altitude_Placeholder)
        self.gridLayout_4.addWidget(self.LatFrame, 1, 0, 1, 1, Qt.AlignBottom)
        self.MapFrame = QWidget(self.MapCombinedFrame)
        self.MapFrame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.MapFrame.sizePolicy().hasHeightForWidth())
        self.MapFrame.setSizePolicy(sizePolicy)
        self.MapFrame.setMinimumSize(QSize(1580, 800))
        self.MapFrame.setMaximumSize(QSize(1580, 800))
        self.MapFrame.setSizeIncrement(QSize(1580, 800))
        self.MapFrame.setBaseSize(QSize(1580, 800))
        self.MapFrame.setFocusPolicy(Qt.WheelFocus)
        self.MapFrame.setWhatsThis("")
        self.MapFrame.setLayoutDirection(Qt.LeftToRight)
        self.MapFrame.setStyleSheet("")
        self.MapFrame.setObjectName("MapFrame")
        self.gridLayout_4.addWidget(self.MapFrame, 0, 0, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)
        self.gridLayout_3.addWidget(self.MapCombinedFrame, 0, 0, 1, 1)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/QSS/icons/map-pin.png"), QIcon.Normal, QIcon.Off)
        self.Tab.addTab(self.Map, icon3, "")
        self.CSVTab = QWidget()
        self.CSVTab.setObjectName("CSVTab")
        self.verticalLayout_2 = QVBoxLayout(self.CSVTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CSV_Display_Text = QLineEdit(self.CSVTab)
        self.CSV_Display_Text.setStyleSheet("background-color: #08122C;\n"
                                            "                                                            color:rgb(243, 255, 6)\n"
                                            "                                                        ")
        self.CSV_Display_Text.setAlignment(Qt.AlignCenter)
        self.CSV_Display_Text.setReadOnly(True)
        self.CSV_Display_Text.setObjectName("CSV_Display_Text")
        self.verticalLayout_2.addWidget(self.CSV_Display_Text)
        self.CSV_Display_Frame = QFrame(self.CSVTab)
        self.CSV_Display_Frame.setFrameShape(QFrame.StyledPanel)
        self.CSV_Display_Frame.setFrameShadow(QFrame.Raised)
        self.CSV_Display_Frame.setObjectName("CSV_Display_Frame")
        self.verticalLayout_2.addWidget(self.CSV_Display_Frame)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/QSS/icons/csv.png"), QIcon.Normal, QIcon.Off)
        self.Tab.addTab(self.CSVTab, icon4, "")
        self.gridLayout.addWidget(self.Tab, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.TabWidget)
        MainWindow.setCentralWidget(self.MainWindow_2)

        self.retranslateUi(MainWindow)
        self.Tab.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dyaus | Cansat"))
        self.CansatLogo.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "hr { height: 1px; border-width: 0; }\n"
                                           "li.unchecked::marker { content: \"\\2610\"; }\n"
                                           "li.checked::marker { content: \"\\2612\"; }\n"
                                           "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/QSS/icons/cansat_logo.jpg\" /></p></body></html>"))
        self.TeamID.setText(_translate("MainWindow", "Team ID : 2022ASI-050"))
        self.TeamName.setText(_translate("MainWindow", "Team Name : Dyaus                 "))
        self.ProgressStateBox.setTitle(_translate("MainWindow", "Progress State"))
        self.ProgressStateBar.setFormat(_translate("MainWindow", "%p%"))
        self.SerialSettings.setText(_translate("MainWindow", "Serial Settings"))
        self.SerialPort.setText(_translate("MainWindow", "Serial Port :"))
        self.PortDropdown.setItemText(0, _translate("MainWindow", "COM1"))
        self.PortDropdown.setItemText(1, _translate("MainWindow", "COM2"))
        self.PortDropdown.setItemText(2, _translate("MainWindow", "COM3"))
        self.PortDropdown.setItemText(3, _translate("MainWindow", "COM4"))
        self.PortDropdown.setItemText(4, _translate("MainWindow", "COM5"))
        self.PortDropdown.setItemText(5, _translate("MainWindow", "COM6"))
        self.PortDropdown.setItemText(6, _translate("MainWindow", "COM7"))
        self.PortDropdown.setItemText(7, _translate("MainWindow", "COM8"))
        self.PortDropdown.setItemText(8, _translate("MainWindow", "COM9"))
        self.PortDropdown.setItemText(9, _translate("MainWindow", "COM10"))
        self.BaudRate.setText(_translate("MainWindow", "Baud Rate :"))
        self.BaudDropdown.setItemText(0, _translate("MainWindow", "57600"))
        self.BaudDropdown.setItemText(1, _translate("MainWindow", "115200"))
        self.BaudDropdown.setItemText(2, _translate("MainWindow", "9600"))
        self.lineEdit.setText(_translate("MainWindow", "Telemetry Data:"))
        self.lineEdit.setReadOnly(True)
        self.Start.setText(_translate("MainWindow", "Start"))
        self.Calibrate.setText(_translate("MainWindow", "Calibrate"))
        self.NirmaLogo.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "hr { height: 1px; border-width: 0; }\n"
                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                          "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/QSS/icons/nirma_logo.jpg\" /></p></body></html>"))
        self.TelemetryDummyGroupBox.setTitle(_translate("MainWindow", "Telemetry"))
        self.TelemetryDummyValues.setHtml(_translate("MainWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "hr { height: 1px; border-width: 0; }\n"
                                                     "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                     "li.checked::marker { content: \"\\2612\"; }\n"
                                                     "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">&lt;TEAM_ID&gt;,&lt;TIME_STAMPING&gt;,&lt;PACKET_COUNT&gt;,&lt;ALTITUDE&gt;,&lt;Pressure&gt;,&lt;Temperature&gt;,&lt;Voltage&gt;,&lt;Hour&gt;,&lt;Minute&gt;,&lt;GNSS_Time_Second&gt;,&lt;GNSS_Location_Latitude&gt;,&lt;GNSS_Location_Langitude&gt;,&lt;GPS_Altitude&gt;,&lt;Connected_Satellites&gt;,&lt;Accelerometer_X&gt;,&lt;Accelerometer_Y&gt;,&lt;Accelerometer_Z&gt;,&lt;ComplementaryRoll&gt;,&lt;ComplementaryPitch&gt;,&lt;ComplementaryYaw&gt;,&lt;Gyro1_Spin&gt;,&lt;Gyro2_Spin&gt;,&lt;State&gt;,&lt;Humidity&gt;,&lt;Velocity&gt;</span>                                                            </p></body></html>"))
        self.TelemetryDummyRealtimeUpdate.setTitle(_translate("MainWindow", "Telementry Data Values"))
        self.AltitudeText.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "hr { height: 1px; border-width: 0; }\n"
                                             "li.unchecked::marker { content: \"\\2610\"; }\n"
                                             "li.checked::marker { content: \"\\2612\"; }\n"
                                             "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Altitude</span>                                                            </p></body></html>"))
        self.SpeedText.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "hr { height: 1px; border-width: 0; }\n"
                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                          "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Velocity</span>                                                            </p></body></html>"))
        self.HumidityText.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "hr { height: 1px; border-width: 0; }\n"
                                             "li.unchecked::marker { content: \"\\2610\"; }\n"
                                             "li.checked::marker { content: \"\\2612\"; }\n"
                                             "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Humidity</span>                                                            </p></body></html>"))
        self.MissionTimeText.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "hr { height: 1px; border-width: 0; }\n"
                                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                "li.checked::marker { content: \"\\2612\"; }\n"
                                                "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">GNSS Time</span>                                                            </p></body></html>"))
        self.LatitiudeText.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "hr { height: 1px; border-width: 0; }\n"
                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                              "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">GNSS Latitude</span>                                                            </p></body></html>"))
        self.LongitudeText.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "hr { height: 1px; border-width: 0; }\n"
                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                              "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">GNSS Longitude</span>                                                            </p></body></html>"))
        self.TimeText.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Mission Time</span>                                                            </p></body></html>"))
        self.PacketCountText.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "hr { height: 1px; border-width: 0; }\n"
                                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                "li.checked::marker { content: \"\\2612\"; }\n"
                                                "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Packet Count</span>                                                            </p></body></html>"))
        self.VoltageText.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "hr { height: 1px; border-width: 0; }\n"
                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Voltage</span>                                                            </p></body></html>"))
        self.TemperatureText.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "hr { height: 1px; border-width: 0; }\n"
                                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                "li.checked::marker { content: \"\\2612\"; }\n"
                                                "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Temperature</span>                                                            </p></body></html>"))
        self.PressureText.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "hr { height: 1px; border-width: 0; }\n"
                                             "li.unchecked::marker { content: \"\\2610\"; }\n"
                                             "li.checked::marker { content: \"\\2612\"; }\n"
                                             "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Pressure</span>                                                            </p></body></html>"))
        self.GPSAltitudeText.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "hr { height: 1px; border-width: 0; }\n"
                                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                "li.checked::marker { content: \"\\2612\"; }\n"
                                                "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">GNSS Altitude</span>                                                            </p></body></html>"))
        self.LatitiudeText_2.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "hr { height: 1px; border-width: 0; }\n"
                                                "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                "li.checked::marker { content: \"\\2612\"; }\n"
                                                "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                                                                </p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Connected Satelites</span>                                                            </p></body></html>"))
        self.ThreeDDataGroupBox.setTitle(_translate("MainWindow", "3D Data"))
        self.Roll.setText(_translate("MainWindow", "Roll"))
        self.AccelerometerYaw.setText(_translate("MainWindow", "TextLabel"))
        self.AccelerometerPitch.setText(_translate("MainWindow", "TextLabel"))
        self.Pitch.setText(_translate("MainWindow", "Pitch"))
        self.Yaw.setText(_translate("MainWindow", "Yaw"))
        self.AccelerometerRoll.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_2.setText(_translate("MainWindow", "3D Graph"))
        self.MagenetometerRoll_2.setText(_translate("MainWindow", "X"))
        self.MagenetometerRoll_3.setText(_translate("MainWindow", "Y"))
        self.MagenetometerRoll_4.setText(_translate("MainWindow", "Z"))
        self.ACCElText.setText(_translate("MainWindow", "ACCEL"))
        self.ACCElXPlaceholder.setText(_translate("MainWindow", "TextLabel"))
        self.ACCElYPlaceholder.setText(_translate("MainWindow", "TextLabel"))
        self.ACCElZPlaceholder.setText(_translate("MainWindow", "TextLabel"))
        self.SpinDial1Placeholder.setText(_translate("MainWindow", "Gyro 1 :"))
        self.SpinDial2Placeholder.setText(_translate("MainWindow", "Gyro 2 :"))
        self.SensorStatus.setTitle(_translate("MainWindow", "Sensor Status"))
        self.Reset_Label.setText(_translate("MainWindow", "Reset"))
        self.IMU_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.Pressure_Label.setText(_translate("MainWindow", "Pressure"))
        self.TEMP_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.RTC_Label.setText(_translate("MainWindow", "RTC"))
        self.RTC_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.IMU_Label.setText(_translate("MainWindow", "IMU"))
        self.RESET_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.PRESSURE_TEXT.setText(_translate("MainWindow", "TextLabel"))
        self.Temp_Label.setText(_translate("MainWindow", "Temp. & Humid."))
        self.Tab.setTabText(self.Tab.indexOf(self.Data), _translate("MainWindow", "Data"))
        self.Humidity_Graph_Text.setText(_translate("MainWindow", "Humidity :"))
        self.Speed_Graph_Text.setText(_translate("MainWindow", "Speed :"))
        self.Temperature_Graph_Text.setText(_translate("MainWindow", "Temperature :"))
        self.Pressure_Graph_Text.setText(_translate("MainWindow", "Pressure :"))
        self.Altitude_Graph_Text.setText(_translate("MainWindow", "Altitude :"))
        self.Voltage_Graph_Text.setText(_translate("MainWindow", "Voltage :"))
        self.Tab.setTabText(self.Tab.indexOf(self.Graph), _translate("MainWindow", "Graph"))
        self.Latitude.setText(_translate("MainWindow", "GNSS Latitude :"))
        self.Longitude.setText(_translate("MainWindow", "GNSS Longitude :"))
        self.GPS_Map_Altitude_Text.setText(_translate("MainWindow", "GNSS Altitude"))
        self.Tab.setTabText(self.Tab.indexOf(self.Map), _translate("MainWindow", "Map"))
        self.CSV_Display_Text.setText(_translate("MainWindow", "flight_050.csv"))
        self.Tab.setTabText(self.Tab.indexOf(self.CSVTab), _translate("MainWindow", "CSV"))
