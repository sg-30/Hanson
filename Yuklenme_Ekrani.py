from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):#yüklenme ekranı
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(1280, 800)
		self.widget = QtWidgets.QWidget(Dialog)
		self.widget.setGeometry(QtCore.QRect(0, -1, 1280, 800))
		self.widget.setStyleSheet("QWidget#widget{\n"
	"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 164, 255, 255), stop:1 rgba(255, 255, 255, 255))}")
		self.widget.setObjectName("widget")
		self.girisResim = QtWidgets.QLabel(self.widget)
		self.girisResim.setGeometry(QtCore.QRect(440, 110, 411, 391))
		self.movie=QtGui.QMovie("images/yukleme.gif",QtCore.QByteArray())
		self.girisResim.setMovie(self.movie)
		self.movie.start()
		self.girisResim.setScaledContents(True)
		self.girisResim.setAlignment(QtCore.Qt.AlignCenter)
		self.girisResim.setWordWrap(False)
		self.girisResim.setObjectName("girisResim")
		self.loadingbar = QtWidgets.QProgressBar(self.widget)
		self.loadingbar.setGeometry(QtCore.QRect(340, 540, 600, 50))
		self.loadingbar.setStyleSheet("QProgressBar {\n"
	"    color: rgb(255, 255, 255);\n"
	"            border-style: none;\n"
	"    background-color: rgb(206, 206, 206);\n"
	"            border-radius: 10px;\n"
	"            text-align: center;\n"
	"            font-size: 30px;\n"
	"        }\n"
	"\n"
	"        QProgressBar::chunk {\n"
	"            border-radius: 10px;\n"
	"    background-color: rgb(41, 176, 156);\n"
	"        }")
		self.loadingbar.setProperty("value", 50)
		self.loadingbar.setAlignment(QtCore.Qt.AlignCenter)
		self.loadingbar.setTextVisible(True)
		self.loadingbar.setObjectName("loadingbar")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


