from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class notlar_ekran(QMainWindow):
	def __init__(self):#not ekranı dizayn bölümü
		super(notlar_ekran, self).__init__()
		self.setObjectName("MainWindow")
		self.resize(901, 700)
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(0, 40, 901, 661))
		self.widget.setObjectName("widget")
		self.scrollArea = QtWidgets.QScrollArea(self.widget)
		self.scrollArea.setGeometry(QtCore.QRect(0, 0, 901, 661))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 899, 659))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
		self.scrollAreaWidgetContents.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 208, 57, 255), stop:0.983051 rgba(202, 255, 83, 255));")
		self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.not_ekle = QtWidgets.QPushButton(self.centralwidget)
		self.not_ekle.setGeometry(QtCore.QRect(550, 10, 150, 25))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(100)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.not_ekle.sizePolicy().hasHeightForWidth())
		self.not_ekle.setSizePolicy(sizePolicy)
		self.not_ekle.setObjectName("not_ekle")
		self.kaydet = QtWidgets.QPushButton(self.centralwidget)
		self.kaydet.setGeometry(QtCore.QRect(740, 10, 150, 25))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(100)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.kaydet.sizePolicy().hasHeightForWidth())
		self.kaydet.setSizePolicy(sizePolicy)
		self.kaydet.setObjectName("kaydet")
		self.kaydet.setCursor(QCursor(Qt.PointingHandCursor))
		self.not_ekle.setCursor(QCursor(Qt.PointingHandCursor))
		self.kaydet.setStyleSheet("border-radius:10px;background-color:rgb(255, 255, 255)")
		self.not_ekle.setStyleSheet("border-radius:10px;background-color:rgb(255, 255, 255)")
		self.setCentralWidget(self.centralwidget)

		dosya=open("dosya.txt","r", encoding='utf-8')
		txt=""
		for x in dosya.readlines():
			txt+=x.replace("\n","")
		self.notlarim=[]
		self.notlarim=txt.split("c-247")

		self.not_ekle.setText( "Not Ekle")
		self.kaydet.setText("Kaydet")
		
		self.text_edit_sayisi=0


		while self.text_edit_sayisi<len(self.notlarim):#kaç tane notumuz olduğunu bulur
			self.text_edit_sayisi+=1

		self.z=0
		self.x=0
		self.not_ekle_button()
		self.not_ekle.clicked.connect(self.not_ekle_button)
		self.kaydet.clicked.connect(self.metin_kaydet)

	def not_ekle_button(self):#yeni not bölümü açıyor
		
		self.x=0
		self.z=0
		while True:
			self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
			self.textEdit.setMinimumSize(QSize(250, 250))
			self.textEdit.setMaximumSize(QSize(250, 250))
			self.textEdit.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
			
			"background-color: rgb(170, 255, 255);\n"
			"font: 12pt \"MS Shell Dlg 2\";\n"
			"color: rgb(0, 0, 127);\n"
			"margin-bottom: 25px;\n"
			"margin-top: 25px;\n"
			"border-radius: 25px;")

			if (self.z*3+self.x)<len(self.notlarim):
				self.textEdit.setText(self.notlarim[(self.z*3+self.x)])
			self.textEdit.setObjectName(str(self.z*3+self.x))
			self.gridLayout.addWidget(self.textEdit, self.z, self.x)
			
			self.x+=1
			if self.x>=3:
				self.x=0
				self.z+=1
			
			if self.text_edit_sayisi==(self.z*3+self.x):#sahip olduğumuz not kadar oluşturduktan sonra while dan çıkarır
				self.text_edit_sayisi+=1
				break

	def metin_kaydet(self):#notları kaydeder
		self.notlarim=[]
		for x in range(self.text_edit_sayisi-1):
			text_id=self.scrollAreaWidgetContents.findChild(QtWidgets.QTextEdit,str(x))
			if text_id.toPlainText()=="":
				for z in range(x,self.text_edit_sayisi-2):
					replace_text1=self.scrollAreaWidgetContents.findChild(QtWidgets.QTextEdit,str(z))
					replace_text2=self.scrollAreaWidgetContents.findChild(QtWidgets.QTextEdit,str(z+1))

					replace_text1.setText(replace_text2.toPlainText())
			self.notlarim.append(text_id.toPlainText())

		gereksiz=self.scrollAreaWidgetContents.findChild(QtWidgets.QTextEdit,str(x-1))

		if text_id.toPlainText() == gereksiz.toPlainText() or text_id.toPlainText()=="":
			self.notlarim[len(self.notlarim)-1]=""
			self.textEdit.setText(self.notlarim[len(self.notlarim)-1])
			self.notlarim.pop()
			self.text_edit_sayisi=len(self.notlarim)
			for i in reversed(range(self.gridLayout.count())): 
				self.gridLayout.itemAt(i).widget().setParent(None)
			self.not_ekle_button()

		dosya=open("dosya.txt","w", encoding='utf-8')
		for item in self.notlarim:
			dosya.write("%s\nc-247\n" % item)
		


