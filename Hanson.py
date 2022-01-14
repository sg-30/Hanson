from PyQt5 import QtCore, QtGui, QtWidgets
from PyGame.pygame_nesne_yakalama import fuzeden_kac
from Shrek.shrektenkac import shrek_oyun
from Qr_kamera_ekran import Qr_kamera
from QR_kamera import Qr_resim_manuel,Qr_resim_otomatik
from hanson_konus_ekran import Ui_anasayfa_ekran_hanson
import sys
from youtube_Ekran import youtube
from notlar_icin import notlar_ekran
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):#Anasayfa
	def setupUi(self, MainWindow):

		self.Qr_kamera= Qr_kamera()

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1280, 800)
		MainWindow.setMinimumSize(1280,800)
		MainWindow.setMaximumSize(1280,800)
		MainWindow.setWindowIcon(QtGui.QIcon('../python arayuz/images/Logo.ico'))

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(0, 0, 1280, 800))

		self.widget.setStyleSheet("QWidget#widget{\n"
				
		"	background-image: url('../python arayuz/images/blue1.jpg');\n"
		"	\n"
		"}\n"
		"#Anasayfa_Button,#Qr_Button,#Oyun_Button,#Notlarim_Button,#Youtube_Button{\n"
		"\n"

		"		background-color: rgb(170, 255, 255);\n"
		"  border-radius: 10px;\n"
		"max-height: 40px;\n"
		"}")
		self.widget.setObjectName("widget")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)#butonlar için düşey sıralama alanı oluşturur
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 200, 230, 520))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		font1 = QFont()
		font1.setFamily(u"Times New Roman")
		font1.setPointSize(14)
		self.Anasayfa_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.Anasayfa_Button.setObjectName("Anasayfa_Button")
		self.Anasayfa_Button.setFont(font1)
		self.Anasayfa_Button.setCursor(QCursor(Qt.PointingHandCursor))
		self.verticalLayout.addWidget(self.Anasayfa_Button)
		self.Qr_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.Qr_Button.setObjectName("Qr_Button")
		self.Qr_Button.setFont(font1)
		self.Qr_Button.setCursor(QCursor(Qt.PointingHandCursor))
		self.verticalLayout.addWidget(self.Qr_Button)
		self.Youtube_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.Youtube_Button.setObjectName("Youtube_Button")
		self.Youtube_Button.setFont(font1)
		self.Youtube_Button.setCursor(QCursor(Qt.PointingHandCursor))
		self.verticalLayout.addWidget(self.Youtube_Button)
		self.Oyun_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.Oyun_Button.setObjectName("Oyun_Button")
		self.Oyun_Button.setFont(font1)
		self.Oyun_Button.setCursor(QCursor(Qt.PointingHandCursor))
		self.verticalLayout.addWidget(self.Oyun_Button)
		self.Notlarim_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.Notlarim_Button.setObjectName("Notlarim_Button")
		self.Notlarim_Button.setFont(font1)
		self.Notlarim_Button.setCursor(QCursor(Qt.PointingHandCursor))
		self.verticalLayout.addWidget(self.Notlarim_Button)
		self.Ekran_Frame = QtWidgets.QFrame(self.widget)#Ekranların açılması için alan oluşturur
		self.Ekran_Frame.setGeometry(QtCore.QRect(310, 20, 951, 761))
		self.Ekran_Frame.setStyleSheet("#Ekran_Frame{background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 208, 57, 255), stop:0.983051 rgba(202, 255, 83, 255));\n""  border-radius: 25px;\n""\n""}\n""")
		self.Ekran_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.Ekran_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Ekran_Frame.setObjectName("Ekran_Frame")
		self.stackedWidget = QtWidgets.QStackedWidget(self.Ekran_Frame)#Sayfa değişimi için değişken alan oluşturur
		self.stackedWidget.setGeometry(QtCore.QRect(10, 9, 930, 740))
		self.stackedWidget.setStyleSheet("")
		self.stackedWidget.setObjectName("stackedWidget")
		self.stackedWidget.addWidget(Ui_anasayfa_ekran_hanson())
		self.QR_Kod_Ekran = QtWidgets.QWidget()
		self.QR_Kod_Ekran.setObjectName("QR_Kod_Ekran")
		self.qr_with_cam = QtWidgets.QPushButton(self.QR_Kod_Ekran)
		self.qr_with_cam.setCursor(QCursor(Qt.PointingHandCursor))
		self.qr_with_cam.setGeometry(QtCore.QRect(120, 150, 240, 230))
		self.qr_with_cam.setStyleSheet("  border: 2px solid blue;\n""background-color: rgb(120, 255, 176);\n""  border-radius: 60px;")
		self.qr_with_cam.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../python arayuz/images/pixlr-bg-result.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.qr_with_cam.setIcon(icon)
		self.qr_with_cam.setIconSize(QtCore.QSize(300, 200))
		self.qr_with_cam.setObjectName("qr_with_cam")
		self.qr_cam_text = QtWidgets.QLabel(self.QR_Kod_Ekran)
		self.qr_cam_text.setGeometry(QtCore.QRect(135, 400, 210, 40))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.qr_cam_text.setFont(font)
		self.qr_cam_text.setAlignment(QtCore.Qt.AlignCenter)
		self.qr_cam_text.setObjectName("qr_cam_text")
		self.qr_ss_text = QtWidgets.QLabel(self.QR_Kod_Ekran)
		self.qr_ss_text.setGeometry(QtCore.QRect(585, 400, 210, 40))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.qr_ss_text.setFont(font)
		self.qr_ss_text.setAlignment(QtCore.Qt.AlignCenter)
		self.qr_ss_text.setObjectName("qr_ss_text")
		self.qr_with_ss = QtWidgets.QPushButton(self.QR_Kod_Ekran)
		self.qr_with_ss.setCursor(QCursor(Qt.PointingHandCursor))
		self.qr_with_ss.setGeometry(QtCore.QRect(570, 150, 240, 230))
		self.qr_with_ss.setStyleSheet("  border: 2px solid blue;\n""background-color: rgb(120, 255, 176);\n""  border-radius: 60px;")
		self.qr_with_ss.setText("")
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("../python arayuz/images/select_area.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.qr_with_ss.setIcon(icon1)
		self.qr_with_ss.setIconSize(QtCore.QSize(300, 200))
		self.qr_with_ss.setObjectName("qr_with_ss")
		self.stackedWidget.addWidget(self.QR_Kod_Ekran)
		self.stackedWidget.addWidget(self.Qr_kamera)
		self.stackedWidget.addWidget(youtube())
		self.Oyun_Ekran = QtWidgets.QWidget()
		self.Oyun_Ekran.setObjectName("Oyun_Ekran")
		self.Game1 = QtWidgets.QPushButton(self.Oyun_Ekran)
		self.Game1.setGeometry(QtCore.QRect(70, 40, 210, 210))
		self.Game1.setAutoFillBackground(False)
		self.Game1.setStyleSheet("background-color: rgb(85, 255, 127);\n""border-radius: 60px;")
		self.Game1.setText("")
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap("../python arayuz/images/ajan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Game1.setIcon(icon2)
		self.Game1.setIconSize(QtCore.QSize(220, 210))
		self.Game1.setShortcut("")
		self.Game1.setAutoRepeat(False)
		self.Game1.setAutoExclusive(False)
		self.Game1.setObjectName("Game1")
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap("../python arayuz/images/shrek.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Game2 = QtWidgets.QPushButton(self.Oyun_Ekran)
		self.Game2.setGeometry(QtCore.QRect(360, 40, 210, 210))
		self.Game2.setStyleSheet("background-color: rgb(85, 255, 127);\n""border-radius: 60px;")
		self.Game2.setText("")
		self.Game2.setIcon(icon3)
		self.Game2.setIconSize(QSize(210, 210))
		self.Game2.setAutoRepeat(False)
		self.Game2.setAutoExclusive(False)
		self.Game2.setObjectName("Game2")
		self.stackedWidget.addWidget(self.Oyun_Ekran)
		self.stackedWidget.addWidget(notlar_ekran())
		self.genel_logo = QtWidgets.QLabel(self.widget)
		self.genel_logo.setGeometry(QtCore.QRect(50, 30, 240, 210))
		self.genel_logo.setText("")
		self.genel_logo.setPixmap(QtGui.QPixmap("../python arayuz/images/Logo.png"))
		self.genel_logo.setScaledContents(True)
		self.genel_logo.setAlignment(QtCore.Qt.AlignCenter)
		self.genel_logo.setObjectName("genel_logo")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.stackedWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Hanson"))
		self.Anasayfa_Button.setText(_translate("MainWindow", "Anasayfa"))
		self.Qr_Button.setText(_translate("MainWindow", "QR"))
		self.Youtube_Button.setText(_translate("MainWindow", "Youtube"))
		self.Oyun_Button.setText(_translate("MainWindow", "Oyun"))
		self.Notlarim_Button.setText(_translate("MainWindow", "Notlarım"))
		self.qr_cam_text.setText(_translate("MainWindow", "Kamera ile Okut"))
		self.qr_ss_text.setText(_translate("MainWindow", "Bilgisayar Ekranından Seç"))

		self.btn_fonksiyonlari()#buton fonksiyonları

	def btn_fonksiyonlari(self):
		self.Anasayfa_Button.clicked.connect(self.anasayfagel)
		self.Qr_Button.clicked.connect(self.qrsayfagel)
		self.qr_with_cam.clicked.connect(self.qrcamscreencome)
		self.qr_with_ss.clicked.connect(self.qrssopen)
		self.Youtube_Button.clicked.connect(self.youtubesayfagel)
		self.Oyun_Button.clicked.connect(self.oyunsayfagel)
		self.Notlarim_Button.clicked.connect(self.notlarsayfagel)
		self.Game1.clicked.connect(self.Game1Acil)
		self.Game2.clicked.connect(self.Game2Acil)

	def anasayfagel(self):#Anasayfayı açar
		self.Qr_kamera.sayfa_degisti()#qr kamerasını kapar
		self.stackedWidget.setCurrentIndex(0)
	def qrsayfagel(self):#QR kod okutma ekranını açar
		self.Qr_kamera.sayfa_degisti()
		self.stackedWidget.setCurrentIndex(1)
	def qrcamscreencome(self):#QR kod kamera ekranını açar
		self.Qr_kamera.kamera_yeni_baslat()#kamerayı açar
		self.stackedWidget.setCurrentIndex(2)
	def youtubesayfagel(self):#Youtube ekranını açar
		self.Qr_kamera.sayfa_degisti()
		self.stackedWidget.setCurrentIndex(3)
	def oyunsayfagel(self):#Oyun ekranını açar
		self.Qr_kamera.sayfa_degisti()
		self.stackedWidget.setCurrentIndex(4)
	def notlarsayfagel(self):#Not ekranını açar
		self.Qr_kamera.sayfa_degisti()
		self.stackedWidget.setCurrentIndex(5)

	def qrssopen(self):#Qr kodu ekrandan okutur
		Qr_resim_manuel()

	def Game1Acil(self):#Ajan oynunu açar
			fuzeden_kac()
	def Game2Acil(self):#Shrek oynunu açar
			shrek_oyun()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
