from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import cv2
from pyzbar import pyzbar
import webbrowser

class Qr_kamera(QWidget):
    def __init__(self):
        super(Qr_kamera, self).__init__()
        self.kameraId=0
        self.available_cameras = QCameraInfo.availableCameras()
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.setWindowTitle("Unreadable Qr Error")
        
        if not self.available_cameras:
            self.error_dialog.showMessage('Please check you Qr')#kameran yoksa hata mesajı döndürür

        self.VBL = QVBoxLayout()
        self.toolbar=QToolBar()
        self.combo=QComboBox()
        self.combo.addItems([camera.description()for camera in self.available_cameras])#kullanmak istediğin kameralar için seçenek oluşturur
        self.toolbar.addWidget(self.combo)
        self.VBL.addWidget(self.toolbar)

        self.FeedLabel = QLabel()
        self.FeedLabel.setAlignment(Qt.AlignCenter)
        self.FeedLabel.setMinimumSize(900,600)
        self.VBL.addWidget(self.FeedLabel)
        self.combo.setCurrentIndex(self.kameraId)
        self.combo.currentIndexChanged.connect(self.kameraSec)
        self.setLayout(self.VBL)

        self.Worker1 = Worker1()
    
    def kamera_yeni_baslat(self):
        self.Worker1 = Worker1()
        self.kameraSec(self.kameraId)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

    def kameraSec(self,i):#seçeneklerden kullanmak istediğin kamerayı seçmeni sağlar
        self.kameraId=i
        self.Worker1.kameraCek(self.kameraId)
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.Worker1.basarili.connect(self.basarili_okundu)
        
    def ImageUpdateSlot(self, Image):
        self.pixmap_image=QPixmap.fromImage(Image)
        self.pixmap_image=self.pixmap_image.scaled(852,580)
        self.FeedLabel.setPixmap(self.pixmap_image)

    def basarili_okundu(self,basarili):#Qr kod düzgün okunursa başarılı mesajını döndürür
        if basarili=="basarili":
            self.FeedLabel.setPixmap(QtGui.QPixmap("../python arayuz/images/Baby-Groot-Transparent.png"))
    
    def sayfa_degisti(self):
        self.Worker1.okundu=True

class Worker1(QThread):#programın işlemesini yavaşlatmaması için thread fonksiyonu oluşturur
    ImageUpdate = pyqtSignal(QImage)
    basarili=pyqtSignal(str)
    def read_barcodes(self,frame):
        barcodes = pyzbar.decode(frame)
        
        if self.okundu==False:
            for barcode in barcodes:
                x, y , w, h = barcode.rect
                barcode_info = barcode.data.decode('utf-8')
                cv2.rectangle(frame, (x, y),(w+x, h+y), (0, 255, 0), 2)
                webbrowser.open(barcode_info)
                self.okundu=True
                break
        
        return frame

    def run(self):
        self.okundu=False
        while self.okundu==False:
            ret, frame = self.Capture.read()
            frame = self.read_barcodes(frame)
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(852, 580, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        
        self.basarili.emit("basarili")
        self.Capture.release()       
        cv2.destroyAllWindows()
        
    def kameraCek(self,kameraId):
        self.kameraId=kameraId
        self.Capture=cv2.VideoCapture(self.kameraId,cv2.CAP_DSHOW)
