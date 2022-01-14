from os import system
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Yuklenme_Ekrani import Ui_Dialog
from Hanson import Ui_MainWindow


# ilk olarak tolga.reg dosyasını çalıştırıp bilgisayarı yeniden başlatarak bilgisayar dilini Türkçe yapıyoruz

# İndirilmesi gereken python ile beraber yüklenmeyen kütüphaneler
# pip install PyQt5
# pip install pygame
# pip install numpy
# pip install opencv-python
# pip install pyzbar
# pip install easy-pil
# pip install pyscreenshot
# pip install PyAutoGUI
# pip install PyScreeze
# pip install pyttsx3
# pip install SpeechRecognition
# pip install wikipedia
# pip install PyQtWebEngine
# pip install pytube




app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()

class LoadingScreen(QMainWindow):#yüklenme ekranımız
	def __init__(self):
		super(LoadingScreen,self).__init__()
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)
		self.setWindowTitle("Hanson")

		self.counter = 0
		self.n = 300#dolum barının genişliği
		self.timer = QTimer()
		self.timer.timeout.connect(self.loading)
		self.timer.start(10)#dolum barının dolma süresini ayarlar
		self.setWindowIcon(QIcon('../python arayuz/images/Logo.ico'))

	def loading(self):#dolum barı %100 olana kadar güncellemek için
		self.ui.loadingbar.setValue(self.counter)
		if self.counter >= self.n:#dolum barı dolduktan sonra yüklenme ekranını kapatıp anasayfa ekranını açar
			self.timer.stop()

			genelekranim= genelEkranim()
			widget.addWidget(genelekranim)
			widget.setCurrentIndex(widget.currentIndex()+1)

		self.counter += 1       
    
class genelEkranim(QMainWindow):#anasayfa ekranı
	def __init__(self):
		super(genelEkranim,self).__init__()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QIcon('../python arayuz/images/Logo.ico'))
		self.setWindowTitle("Hanson")



loading = LoadingScreen()
widget.addWidget(loading)
widget.setWindowIcon(QIcon('../python arayuz/images/Logo.ico'))
widget.setWindowTitle("Hanson")
widget.setFixedWidth(1280)
widget.setFixedHeight(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Çıkış Yapılıyor...")
    
    
    
    
    
    