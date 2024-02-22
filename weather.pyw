#Thanks for download my project
#by Ilya

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, qApp
from PyQt5.QtCore import QCoreApplication, Qt
import datetime
import requests
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 200, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/2.png"))
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: transparent")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 160, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: transparent")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 30, 30))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resources/3-30x30.png"))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-color: transparent")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 180, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/4-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: transparent")
        self.pushButton.enterEvent(self.pushButton.setStyleSheet("background-color: Light Grey"))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 180, 200, 30))
        self.lineEdit.setStyleSheet("background-color: rgb(220, 220, 220);\n""font: 8pt \"Comfortaa\";")
        self.lineEdit.setObjectName("lineEdit")

        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setGeometry(QtCore.QRect(100, 210, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        self.warning.setFont(font)
        self.warning.setStyleSheet("color: rgb(255, 0, 0);")
        self.warning.setObjectName("warning")
        self.warning.hide()

        self.line = QtWidgets.QLabel(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 380, 360, 10))
        self.line.setPixmap(QtGui.QPixmap("resources/line.png"))
        self.line.setText("")
        self.line.setObjectName("Line")
        self.line.setAlignment(Qt.AlignCenter)
        self.line.setStyleSheet("background-color: transparent")
        self.line.hide()

        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(140, 200, 112, 112))
        self.Image.setText("")
        self.Image.setObjectName("Image")
        self.Image.setAlignment(Qt.AlignCenter)
        self.Image.setStyleSheet("background-color: transparent")
        self.Image.hide()

        self.ImageSTR = QtWidgets.QLabel(self.centralwidget)
        self.ImageSTR.setGeometry(40, 20, 175, 290)
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(11)
        self.ImageSTR.setFont(font)
        self.ImageSTR.setObjectName("ImageSTR")
        self.ImageSTR.setAlignment(Qt.AlignCenter)
        self.ImageSTR.setStyleSheet("background-color: transparent")
        self.ImageSTR.hide()

        self.Descripton = QtWidgets.QLabel(self.centralwidget)
        self.Descripton.setGeometry(QtCore.QRect(159, 310, 80, 16))
        self.Descripton.setObjectName("Descripton")
        self.Descripton.setStyleSheet("background-color: transparent")
        self.Descripton.hide()

        self.TempICO = QtWidgets.QLabel(self.centralwidget)
        self.TempICO.setGeometry(QtCore.QRect(20, 330, 50, 50))
        self.TempICO.setText("")
        self.TempICO.setPixmap(QtGui.QPixmap("resources/temp1.png"))
        self.TempICO.setObjectName("TempIco")
        self.TempICO.setStyleSheet("background-color: transparent")
        self.TempICO.hide()

        self.TempSTR = QtWidgets.QLabel(self.centralwidget)
        self.TempSTR.setGeometry(QtCore.QRect(59, 330, 50, 50))
        self.TempSTR.setText("17°C")
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(16)
        self.TempSTR.setFont(font)
        self.TempSTR.setObjectName("TempSTR")
        self.TempSTR.setStyleSheet("background-color: transparent")
        self.TempSTR.hide()

        self.FeelsLikeICO = QtWidgets.QLabel(self.centralwidget)
        self.FeelsLikeICO.setGeometry(QtCore.QRect(135, 330, 50, 50))
        self.FeelsLikeICO.setText("")
        self.FeelsLikeICO.setPixmap(QtGui.QPixmap("resources/feels like.png"))
        self.FeelsLikeICO.setObjectName("FeelsLikeICO")
        self.FeelsLikeICO.setStyleSheet("background-color: transparent")
        self.FeelsLikeICO.hide()

        self.FeelsLikeSTR = QtWidgets.QLabel(self.centralwidget)
        self.FeelsLikeSTR.setGeometry(QtCore.QRect(185, 330, 50, 50))
        self.FeelsLikeSTR.setText("22°C")
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(16)
        self.FeelsLikeSTR.setFont(font)
        self.FeelsLikeSTR.setObjectName("FeelsLikeSTR")
        self.FeelsLikeSTR.setStyleSheet("background-color: transparent")
        self.FeelsLikeSTR.hide()

        self.VisibilityICO = QtWidgets.QLabel(self.centralwidget)
        self.VisibilityICO.setGeometry(QtCore.QRect(260, 330, 50, 50))
        self.VisibilityICO.setText("")
        self.VisibilityICO.setPixmap(QtGui.QPixmap("resources/visibility.png"))
        self.VisibilityICO.setObjectName("visibilityICO")
        self.VisibilityICO.setStyleSheet("background-color: transparent")
        self.VisibilityICO.hide()

        self.VisibilitySTR = QtWidgets.QLabel(self.centralwidget)
        self.VisibilitySTR.setGeometry(QtCore.QRect(310, 330, 70, 50))
        self.VisibilitySTR.setText("0.5km")
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(16)
        self.VisibilitySTR.setFont(font)
        self.VisibilitySTR.setObjectName("VisibilitySTR")
        self.VisibilitySTR.setStyleSheet("background-color: transparent")
        self.VisibilitySTR.hide()

        self.PressureICO = QtWidgets.QLabel(self.centralwidget)
        self.PressureICO.setGeometry(QtCore.QRect(15, 400, 50, 50))
        self.PressureICO.setText("")
        self.PressureICO.setPixmap(QtGui.QPixmap("resources/pressure2.png"))
        self.PressureICO.setObjectName("PressureICO")
        self.PressureICO.setStyleSheet("background-color: transparent")
        self.PressureICO.hide()

        self.PressureSTR = QtWidgets.QLabel(self.centralwidget)
        self.PressureSTR.setGeometry(QtCore.QRect(60, 400, 90, 50))
        self.PressureSTR.setText("1031hPa")
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(16)
        self.PressureSTR.setFont(font)
        self.PressureSTR.setObjectName("PressureSTR")
        self.PressureSTR.setStyleSheet("background-color: transparent")
        self.PressureSTR.hide()

        self.HumidityICO = QtWidgets.QLabel(self.centralwidget)
        self.HumidityICO.setGeometry(QtCore.QRect(160, 400, 50, 50))
        self.HumidityICO.setText("")
        self.HumidityICO.setPixmap(QtGui.QPixmap("resources/humidity1.png"))
        self.HumidityICO.setObjectName("HumidityICO")
        self.HumidityICO.setStyleSheet("background-color: transparent")
        self.HumidityICO.hide()

        self.HumiditySTR = QtWidgets.QLabel(self.centralwidget)
        self.HumiditySTR.setGeometry(QtCore.QRect(200, 400, 50, 50))
        self.HumiditySTR.setText("78%")
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(16)
        self.HumiditySTR.setFont(font)
        self.HumiditySTR.setObjectName("HumiditySTR")
        self.HumiditySTR.setStyleSheet("background-color: transparent")
        self.HumiditySTR.hide()

        self.WindICO = QtWidgets.QLabel(self.centralwidget)
        self.WindICO.setGeometry(QtCore.QRect(265, 400, 50, 50))
        self.WindICO.setText("")
        self.WindICO.setPixmap(QtGui.QPixmap("resources/wind.png"))
        self.WindICO.setObjectName("WindICO")
        self.WindICO.setStyleSheet("background-color: transparent")
        self.WindICO.hide()

        self.WindSTR = QtWidgets.QLabel(self.centralwidget)
        self.WindSTR.setGeometry(QtCore.QRect(310, 400, 90, 50))
        self.WindSTR.setText("0.5m/s")
        font = QtGui.QFont()
        font.setFamily("Comfortaa")
        font.setPointSize(16)
        self.WindSTR.setFont(font)
        self.WindSTR.setObjectName("WindSTR")
        self.WindSTR.setStyleSheet("background-color: transparent")
        self.WindSTR.hide()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.backend)

    def backend(self):
        self.warning.hide()

        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = open("resources/API_KEY.txt", "r").read()
        LOCATION = self.lineEdit.text()
        get = True

        url = BASE_URL + "appid=" + API_KEY + "&q=" + LOCATION

        try:
            response = requests.get(url).json()

            kelvin = response["main"]["temp"]
            celsius = kelvin - 273.15
            fahrenheit = celsius * (9 / 5) + 32

            kelvinFeelLike = response["main"]["feels_like"]
            celsiusFeelsLike = kelvinFeelLike - 273.15
            fahrenheitFeelsLike = celsiusFeelsLike * (9 / 5) + 32

            celsius = int(round(celsius, 0))
            celsiusFeelsLike = int(round(celsiusFeelsLike, 0))

            if celsius <= 0:
                celsius = str(int(celsius))
            else:
                celsius = "+" + str(celsius)

            if celsiusFeelsLike <= 0:
                celsiusFeelsLike = str(int(celsiusFeelsLike))
            else:
                celsiusFeelsLike = str(celsius)


            description = response["weather"][0]["description"]

            visibility = response["visibility"] / 1000
            visibility = round(visibility, 1)
            pressure = response["main"]["pressure"]
            humidity = response["main"]["humidity"]
            wind = response["wind"]["speed"]

        except KeyError:
            self.warning.show()

            self.line.hide()
            self.Image.hide()
            self.ImageSTR.hide()
            self.Descripton.hide()
            self.TempICO.hide()
            self.TempSTR.hide()
            self.FeelsLikeICO.hide()
            self.FeelsLikeSTR.hide()
            self.VisibilityICO.hide()
            self.VisibilitySTR.hide()
            self.PressureICO.hide()
            self.PressureSTR.hide()
            self.HumidityICO.hide()
            self.HumiditySTR.hide()
            self.WindICO.hide()
            self.WindSTR.hide()

            get = False

        if get:
            icon_1 = response["weather"][0]["main"]
            if response["weather"][0]["main"] == "Clear":
                icon_1 = response["weather"][0]["main"]
            elif response["weather"][0]["main"] == "Clouds" and response["weather"][0]["description"] == "overcast clouds":
                icon_1 = response["weather"][0]["description"]
            elif response["weather"][0]["main"] == "Clouds" and response["weather"][0]["description"] != "overcast clouds":
                icon_1 = "Clouds"
            elif response["weather"][0]["main"] == "Haze":
                icon_1 = "Fog"
            elif response["weather"][0]["main"] == "Mist":
                icon_1 = "Fog"
            elif response["weather"][0]["main"] == "Rain" and response["weather"][0]["description"] == "light rain":
                icon_1 = response["weather"][0]["description"]
            elif response["weather"][0]["main"] == "Snow" and response["weather"][0]["description"] == "light snow":
                icon_1 = response["weather"][0]["description"]
            elif response["weather"][0]["main"] == "Rain" and response["weather"][0]["description"] == "moderate rain" or "rain":
                icon_1 = response["weather"][0]["description"]
            elif response["weather"][0]["main"] == "Snow" and response["weather"][0]["description"] == "light shower snow":
                icon_1 = response["weather"][0]["description"]
            elif response["weather"][0]["main"] == "Rain" and response["weather"][0]["description"] == "heavy rain" or "very heavy rain":
                icon_1 = response["weather"][0]["description"]
            elif response["weather"][0]["main"] == "Smoke" or "Fog" or "Mist" or "Haze" and response["weather"][0]["description"] == "smoke" or "fog" or "mist" or "haze":
                icon_1 = "Fog"

            self.line.show()

            self.Image.show()
            self.Image.setPixmap(QtGui.QPixmap("resources/" + icon_1 + ".png"))

            self.ImageSTR.show()
            self.ImageSTR.setText(response["weather"][0]["main"])
            if self.ImageSTR.text() == "Clear":
                self.ImageSTR.setGeometry(175, 290, 40, 20)
            elif self.ImageSTR.text() == "Clouds":
                self.ImageSTR.setGeometry(168, 290, 60, 20)
            elif self.ImageSTR.text() == "Fog":
                self.ImageSTR.setGeometry(183, 295, 30, 25)
            elif self.ImageSTR.text() == "Mist":
                self.ImageSTR.setGeometry(183, 295, 30, 25)
            elif self.ImageSTR.text() == "Smoke":
                self.ImageSTR.setGeometry(153, 290, 90, 25)
            elif self.ImageSTR.text() == "Haze":
                self.ImageSTR.setGeometry(153, 290, 90, 25)
            elif self.ImageSTR.text() == "Snow":
                self.ImageSTR.setGeometry(175, 295, 40, 20)
            elif self.ImageSTR.text() == "Rain":
                self.ImageSTR.setGeometry(175, 295, 40, 20)

            self.Descripton.show()
            self.Descripton.setText(str(description).capitalize())
            if self.Descripton.text() == self.ImageSTR.text():
                self.Descripton.hide()

            if self.Descripton.text() == "Clear sky":
                self.Descripton.setGeometry(173, 310, 80, 16)
            elif self.Descripton.text() == "Few clouds":
                self.Descripton.setGeometry(173, 310, 80, 16)
            elif self.Descripton.text() == "Overcast clouds":
                self.Descripton.setGeometry(159, 310, 80, 16)
            elif self.Descripton.text() == "Broken clouds":
                self.Descripton.setGeometry(165, 310, 80, 16)
            elif self.Descripton.text() == "Scattered clouds":
                self.Descripton.setGeometry(159, 310, 80, 16)
            elif self.Descripton.text() == "Light shower snow":
                self.Descripton.setGeometry(150, 310, 90, 25)
            elif self.Descripton.text() == "Light snow":
                self.Descripton.setGeometry(170, 310, 50, 25)
            elif self.Descripton.text() == "Light rain":
                self.Descripton.setGeometry(173, 310, 50, 25)
            elif self.Descripton.text() == "Moderate rain":
                self.Descripton.setGeometry(160, 310, 70, 25)

            self.TempICO.show()
            self.TempSTR.show()
            self.TempSTR.setText(str(celsius))

            self.FeelsLikeICO.show()
            self.FeelsLikeSTR.show()
            self.FeelsLikeSTR.setText(str(celsiusFeelsLike))

            self.VisibilityICO.show()
            self.VisibilitySTR.show()
            self.VisibilitySTR.setText(str(visibility) + "km")

            self.PressureICO.show()
            self.PressureSTR.show()
            self.PressureSTR.setText(str(pressure) + "hPa")

            self.HumidityICO.show()
            self.HumiditySTR.show()
            self.HumiditySTR.setText(str(humidity) + "%")

            self.WindICO.show()
            self.WindSTR.show()
            self.WindSTR.setText(str(wind) + "m/s")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Погода"))
        self.label_2.setText(_translate("MainWindow", "Enter your location..."))
        self.warning.setText(_translate("MainWindow", "Некорректное название местности"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
