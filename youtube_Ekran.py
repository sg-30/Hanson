from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import re
from os.path import expanduser
import time
from pytube import YouTube


class youtube(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
        self.anaAyarlar()

    def anaAyarlar(self):
        self.setMinimumSize(QSize(900, 700))
        self.setMaximumSize(QSize(900, 700))
        self.movie = QMovie("images/spinner2.gif")
        self.movie.setScaledSize(QSize(550,550))

    def setUI(self):
        self.isDownloadable = False
        self.v_box = QVBoxLayout()
        self.v_box.setAlignment(Qt.AlignTop)
        widget1 = self.anaWidget()
        self.v_box.addWidget(widget1)
        self.videoAlaniWidget = QWidget()
        self.thumbnailAlaniWidget = QWidget()
        self.beklemeEkraniWidget = QWidget()
        self.altAlanStack = QStackedWidget()
        self.altAlanStack.addWidget(self.beklemeEkraniWidget)  
        self.altAlanStack.addWidget(self.thumbnailAlaniWidget)
        self.v_box.addWidget(self.altAlanStack)
        ana_widget = QWidget()
        ana_widget.setLayout(self.v_box)
        self.setCentralWidget(ana_widget)

    def anaWidget(self):#buraya kadar youtube ekran dizaynını sağlar
        widget = QWidget()
        v_box = QVBoxLayout()
        v_box.setAlignment(Qt.AlignTop)
        h_box = QHBoxLayout()
        videoIndirYazi = QLabel("<b>Video Linki</b> : ")
        self.linkGiris = QLineEdit()
        self.linkGiris.setPlaceholderText("Youtube Linki...")
        self.linkGiris.textChanged.connect(self.goster)
        self.indirButton = QPushButton()
        self.indirButton.setIcon(QIcon("images/download.png"))
        self.indirButton.setIconSize(QSize(35, 35))
        self.indirButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.indirButton.setToolTip("İndir")
        self.indirButton.setEnabled(self.isDownloadable)
        self.indirButton.clicked.connect(self.downloadVideos)
        h_box.addWidget(videoIndirYazi)
        h_box.addWidget(self.linkGiris)
        h_box.addWidget(self.indirButton)
        h_box.setAlignment(Qt.AlignTop)
        v_box.addLayout(h_box)
        widget.setLayout(v_box)

        return widget

    def downloadVideos(self):#videonun ineceği yeri seçtirir
        dosyaYolu = QFileDialog.getExistingDirectory(self,"İndirilecek dosyalar için klasör seçin",expanduser("~"),QFileDialog.ShowDirsOnly)

        if dosyaYolu != "":
            self.indirButton.setEnabled(False)
            self.linkGiris.setEnabled(False)

            self.movie.stop()
            widget = QWidget()
            v_box = QVBoxLayout()
            v_box.setAlignment(Qt.AlignTop)
            self.spinner = QLabel("")
            self.spinner.setAlignment(Qt.AlignHCenter)
            self.spinner.setMovie(self.movie)
            self.movie.start()
            v_box.addWidget(self.spinner)
            widget.setLayout(v_box)
            self.altAlanStack.insertWidget(2,widget)
            self.altAlanStack.setCurrentIndex(2)
            self.indirme = Download(YouTube(self.gelenLink),dosyaYolu,"mp4")
            self.indirme.authResult.connect(self.bitti)
            self.indirme.start()
        
    def bitti(self):#indirmenin bittiği mesajını döndürür
        widget = QWidget()
        v_box = QVBoxLayout()
        v_box.setAlignment(Qt.AlignTop)
        basarili = QLabel("")
        resim = QPixmap("images/success.png")
        resim = resim.scaled(500,500)
        basarili.setPixmap(resim)
        basarili.setAlignment(Qt.AlignHCenter)
        bilgiVer = QLabel("<b>Video <font color='green'>Başarıyla</font> İndirildi</b>")
        bilgiVer.setAlignment(Qt.AlignHCenter)
        v_box.addWidget(bilgiVer)
        v_box.addWidget(basarili)
        widget.setLayout(v_box)
        self.altAlanStack.insertWidget(2, widget)
        self.altAlanStack.setCurrentIndex(2)
        self.indirButton.setEnabled(True)
        self.linkGiris.setEnabled(True)

    def controlYoutubeLink(self, url):#linki kontrol eder
        youtube_regex = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
        youtube_regex_match = re.match(youtube_regex, url)
        if youtube_regex_match:
            self.isDownloadable = True
            return True
        self.isDownloadable = False
        return False

    def yuklemeAlani(self):
        self.movie.stop()
        widget = QWidget()
        v_box = QVBoxLayout()
        v_box.setAlignment(Qt.AlignTop)
        self.spinner = QLabel()
        self.spinner.setAlignment(Qt.AlignHCenter)
        self.spinner.setMovie(self.movie)
        self.movie.start()
        v_box.addWidget(self.spinner)
        widget.setLayout(v_box)
        self.altAlanStack.insertWidget(2,widget)
        self.altAlanStack.setCurrentIndex(2)

    def videoAlaniOlustur(self, video):#videoyu ekranda izlememizi sağlar
        widget = QWidget()
        v_box = QVBoxLayout()
        v_box.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        webwiev = QWebEngineView()
        webwiev.page().setBackgroundColor(Qt.transparent)
        html = """<center><iframe width="870" height="550" src="https://www.youtube.com/embed/{}" frameborder="0" allow="accelerometer; 
                autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>""".format(video.split("=")[1])
        webwiev.setFixedSize(900,600)
        webwiev.setHtml(html)
        v_box.addWidget(webwiev)
        widget.setLayout(v_box)
        self.movie.stop()
        self.altAlanStack.insertWidget(1,widget)
        self.altAlanStack.setCurrentIndex(1)
        self.indirButton.setEnabled(self.isDownloadable)

    def goster(self):#videoyu açar
        self.indirButton.setEnabled(False)
        self.yuklemeAlani()
        self.gelenLink = self.linkGiris.text()
        isYoutube = self.controlYoutubeLink(self.gelenLink)
        if isYoutube:
            self.gorev2 = GorevVideo(self.gelenLink)
            self.gorev2.authResult.connect(self.videoAlaniOlustur)
            self.gorev2.start()

class GorevVideo(QThread):#videoyu ekranda açtırır
    authResult = pyqtSignal(object)
    def __init__(self, link):
        super().__init__()
        self.gelenLink = link
    def run(self):
        time.sleep(2)
        self.authResult.emit(self.gelenLink)

class Download(QThread):#videoyu indirmemizi sağlar
    authResult = pyqtSignal(object)

    def __init__(self, video,yol,tur):
        super().__init__()
        self.video = video
        self.yol = yol
        self.tur = tur
        self.isim = re.sub('[^A-Za-z0-9]+', '', self.video.title)+".mp4"
    def run(self):
        if self.tur == "mp4":
            self.video.streams.filter(resolution="720p", mime_type="video/mp4").first().download(self.yol,filename=self.isim)
        self.authResult.emit(self.isim)