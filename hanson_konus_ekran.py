import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import time
import numpy as np
import sounddevice as sd
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_anasayfa_ekran_hanson(QtWidgets.QWidget):
	def __init__(self):#hanson sayfasının dizayn bölümü
		super(Ui_anasayfa_ekran_hanson, self).__init__()
		global stop_threads
		self.bulundu=1
		self.sadece_1_kez_calis=0
		
		self.setObjectName("anasayfa_ekran_hanson")
		self.resize(930, 740)
		self.Kullanici_konusuyor = QtWidgets.QLabel(self)
		self.Kullanici_konusuyor.setGeometry(QtCore.QRect(315, 640, 300, 60))
		self.Kullanici_konusuyor.setAlignment(QtCore.Qt.AlignCenter)
		self.Kullanici_konusuyor.setObjectName("Kullanici_konusuyor")
		font = QtGui.QFont()
		font.setPointSize(16)
		self.Kullanici_konusuyor.setFont(font)
		self.Ses_analiz_label = QtWidgets.QLabel(self)
		self.Ses_analiz_label.setGeometry(QtCore.QRect(175, 450, 580, 150))
		self.Ses_analiz_label.setAlignment(QtCore.Qt.AlignCenter)
		self.Ses_analiz_label.setObjectName("Ses_analiz_label")
		self.baslat_button = QtWidgets.QPushButton(self)
		self.baslat_button.setGeometry(QtCore.QRect(340, 390, 111, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.baslat_button.setFont(font)
		self.baslat_button.setObjectName("pushButton")
		self.durdur_button = QtWidgets.QPushButton(self)
		self.durdur_button.setGeometry(QtCore.QRect(480, 390, 111, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.durdur_button.setFont(font)
		self.durdur_button.setObjectName("pushButton_2")
		self.Anasayfa_Resim = QtWidgets.QLabel(self)
		self.Anasayfa_Resim.setGeometry(QtCore.QRect(315, 100, 300, 280))
		self.Anasayfa_Resim.setText("")
		self.movie=QtGui.QMovie("images/Hanson.gif",QtCore.QByteArray())
		self.Anasayfa_Resim.setMovie(self.movie)
		self.movie.start()
		self.Anasayfa_Resim.setScaledContents(True)
		self.Anasayfa_Resim.setAlignment(QtCore.Qt.AlignCenter)
		self.Anasayfa_Resim.setObjectName("Anasayfa_Resim")

		self.baslat_button.setText("Başlat")
		self.baslat_button.setStyleSheet("border-radius:20px;background-color:rgb(255, 255, 255)")
		self.durdur_button.setText("Kapat")
		self.durdur_button.setStyleSheet("border-radius:20px;background-color:rgb(255, 255, 255)")
		self.baslat_button.setCursor(QCursor(Qt.PointingHandCursor))
		self.durdur_button.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_fonksiyonlari()#buton fonksiyonlarını çağırır

	def btn_fonksiyonlari(self):
		self.baslat_button.clicked.connect(self.baslat_buton_aktif)
		self.durdur_button.clicked.connect(self.durdur_buton_aktif)

	def baslat_buton_aktif(self):#Hanson ı çağırır
		if self.sadece_1_kez_calis==0:
			self.sadece_1_kez_calis=1
			self.Kullanici_konusuyor.setText("...")
			self.t2 = threading.Thread(target=self.draw_Voice)
			self.t1 = threading.Thread(target=self.konustur)
			self.stop_threads = False
			self.sleepint=10000
			self.t2.start()
			self.t1.start() 
		
	def durdur_buton_aktif(self):#Hanson ı kapatır
		if self.sadece_1_kez_calis==1:
			self.Kullanici_konusuyor.setText("Kapanıyor...")
		
		self.stop_threads = True
		self.sleepint=0

	def draw_Voice(self):#analiz ettiği sesi çizer
		self.dizi=[]
		self.metin=[]
		self.yatay=200
		self.dikey=5
		for x in range(self.yatay):
			self.dizi.append(0)
		def print_sound(indata, outdata, frames, time, status):
			if self.stop_threads==False:
				self.metin=[]
				txt=""  
				i=np.linalg.norm(indata)*3/7
				if i>9:
					i=9
				self.dizi.pop(0)
				self.dizi.append(i)

				a=self.dikey
				for z in range(self.dikey):
					txt=""
					for x in range(self.yatay):
						if a<=self.dizi[x]:
							txt+="|"
						else:
							txt+="-"
					a=a-1
					self.metin.append(txt)
				
				txt=""
				for x in self.metin:
					txt+=x+"\n"
				for x in range(self.yatay):
					txt+="|"
				txt+="\n"
				for x in reversed(self.metin):
					txt+=x+"\n"

				self.Ses_analiz_label.setText(txt)
			
		with sd.Stream(callback=print_sound):
			while True:
				sd.play(5,48000)
				if self.stop_threads:
					sd.stop()
					break

	def speak(self,audio):#hanson ın konuşmasını sağlar
		try:
			if self.stop_threads==False and self.sadece_1_kez_calis==1:
				engine = pyttsx3.init()
				voices = engine.getProperty('voices')
				engine. setProperty("rate", 174)
				for voice in voices:
					if "Tolga" in voice.name:
						engine.setProperty('voice', voice.id)
						break
				engine.say(audio)
				engine.runAndWait()
		except:
			pass

	def time_(self):#saati söyler
		Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
		self.speak("saat")
		self.speak(Time)
		Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
		self.speak(Time)                                  

	def date_(self):#tarihi söyler
		year = datetime.datetime.now().year
		month = datetime.datetime.now().month
		day = datetime.datetime.now().day
		self.speak("tarih")
		self.speak(day)
		self.speak(month)
		self.speak(year)
						
	def wishme(self):#giriş konuşması
		self.speak("Hoşgeldiniz!")
		hour = datetime.datetime.now().hour
		if hour>=6 and hour <12:
			self.speak("Günaydın!")
		elif hour>=12 and hour<18:
			self.speak("Tünaydın!")
		elif hour>=18 and hour<24:
			self.speak("İyi akşamlar!")
		else:
			self.speak("İyi geceler!")
		self.speak("Hensın hizmetinizde size nasıl yardımcı olabilirim?")

	def TakeCommand(self):#burada bizden istek alıyor
		self.yazmaefekti=[]
		r = sr.Recognizer()
		r.energy_threshold=4000
		query=""
		
		if self.stop_threads==False:
			if self.bulundu==0:
				self.Kullanici_konusuyor.setText("TANIMLANAMADI!")
				self.speak("Maalesef öyle bir özelliğim bulunmamakta, başka bir isteğiniz?")
			with sr.Microphone() as source:
				self.Kullanici_konusuyor.setText("dinleniyor")
				self.speak("dinleniyor")
				audio = r.listen(source,phrase_time_limit=8)
			try:
				query = r.recognize_google(audio,language='tr-TR')
				for x in query:
					self.yazmaefekti.append(x)
					txt=""
					for z in self.yazmaefekti:
						txt+=z
					self.Kullanici_konusuyor.setText(txt+"...")
					time.sleep(0.2)
				time.sleep(1)
			
			except Exception as e:
				self.Kullanici_konusuyor.setText("tekrar söyleyebilir misiniz?")
				self.speak("tekrar söyleyebilir misiniz?")
				return "Anlayamadım"
		return query                         

	def screenshot(self):#ekran fotoğrafı alır
		img = pyautogui.screenshot()
		img.save("../screenshot.png")
																										
	def konustur(self):#Hanson ile iletişimi başlatır
		self.wishme()
		while True:
			query = self.TakeCommand().lower()
			self.bulundu=0
			
			if "anlayamadım" in query:
				self.bulundu=1

			elif 'saat' in query:
				self.bulundu=1
				self.time_()

			elif 'tarih' in query:
				self.bulundu=1
				self.date_()
			
			elif 'wikipedia' in query:#wikipedia da araştırma yapar
				self.bulundu=1
				self.speak("araştırılıyor")
				query = query.replace("Wikipedia",'')
				result = wikipedia.summary(query,sentences = 3)
				self.speak("vikipedyaya göre..")
				print(result)
				self.speak(result)
			
			elif "youtube'da araştır" in query:#youtube da video başlığı aratır
				self.bulundu=1
				self.speak("ne aratmamı istersiniz")
				search_Term = self.TakeCommand().lower()
				self.speak("yutuba gidiyoruz")
				wb.open("https://www.youtube.com/results?search_query="+search_Term)
			
			elif "google" in query:#google da araştırma yapar
				self.bulundu=1
				self.speak("ne araştırmamı istersiniz")
				search_Term = self.TakeCommand().lower()
				wb.open("https://www.google.com/search?q="+search_Term)

			elif 'sistemi kapat' in query:#hanson ı durdurur
				self.bulundu=1
				self.speak("kapatılıyor")
				self.durdur_buton_aktif()

			elif 'ekran görüntüsü' in query:#ekran görüntüsü aldırır
				self.bulundu=1
				self.screenshot()

			elif "aklında tut" in query:#aklında tutmasını istediğiniz konuyu ezberler
				self.bulundu=1
				self.speak("neyi aklımda tutmalıyım")
				memory = self.TakeCommand()
				self.speak("şunu aklımda tutmamı istediniz: "+memory)
				remember = open("memory.txt","w")
				remember.write(memory)
				remember.close()

			elif "bir şey hatırlıyor musun" in query:#aklında tutmasını istediğimiz konuları söyler
				self.bulundu=1
				remember = open("memory.txt","r")
				self.speak("bunu hatırlamamı istediniz"+remember.read()) 

			elif "nerede" in query:#merak ettiğimiz bir yerin konumunu söyler
				self.bulundu=1
				query = query.replace("where is","")
				location = query
				wb.open_new_tab("https://www.google.com/maps/place/"+location)  
			
			elif "bilgisayarı yeniden başlat" in query:
				self.bulundu=1
				os.system("shutdown /r /t 1")

			elif "bilgisayarı kapat" in query:
				self.bulundu=1
				os.system("shutdown /s /t 1")

			elif "nasılsın" in query:#buradan sonrası sohbet için
				self.bulundu=1
				self.speak("Çok iyi , sen nasılsın")
			elif "adın ne" in query:
				self.bulundu=1
				self.speak("adım hensın ,görevim sana yardımcı olmak,burcum oğlak yani bana güvenebilirsin")
			elif "işin ne" in query:
				self.bulundu=1
				self.speak("işim senin hayatını kolaylaştırmak,yapmamı istediğin bir şey varsa lütfen söyle")
			elif " seviyor musun" in query:
				self.bulundu=1
				self.speak("hem de çok ")
			elif "sevdiğini söyle" in query:
				self.bulundu=1
				self.speak("seni seviyorum")
			elif "teşekkür ederim" in query:
				self.bulundu=1
				self.speak("ne demek")
			elif "görüşürüz" in query:
				self.bulundu=1
				self.speak("görüşürüz")
			elif "iyi geceler" in query:
				self.bulundu=1
				self.speak("mışıl mışıl uyu")
			elif "iyi akşamlar" in query:
				self.bulundu=1
				self.speak("sana da iyi akşamlar")
			elif "bay" in query:
				self.bulundu=1
				self.speak("bay bay")
			elif "komiksin" in query:
				self.bulundu=1
				self.speak("seni güldürebildiğimde iyi hissediyorum")
			elif "şarkı söyle" in query:
				self.bulundu=1
				self.speak("çok mutluyum yum yum yum,neşe doluyum yum yum ,ne şanslı bir asistanım nım nım nım,sensin benim yıldızım zım zım zım")
			elif "günaydın" in query:
				self.bulundu=1
				self.speak("günaydın")
			elif "ne yapıyorsun" in query:
				self.bulundu=1
				self.speak("yeni şeyler seni şımartmak için en güzel kelimeleri seçmeye çalışıyorum.duymak istersen iltifat et demen yeterli")
			elif "iltifat et" in query:
				self.bulundu=1
				self.speak("istediğin iltifat olsun.herkesin hayatında bir sen olmalı")
			elif "bana iltifat et" in query:
				self.bulundu=1
				self.speak("sen aklına koyduğun her şeyi başarırsın çünkü senin inanılmaz bir gücün var ve kalbin de var")
			elif "gül" in query:
				self.bulundu=1
				self.speak("HAHAHAHAHA")
			elif "ilginç bilgi" in query:
				self.bulundu=1
				self.speak("ben bunu çok ilginç bulmuştum.koalalar günde 20 saate kadar uyuyabilirler")
			elif "bana ilginç bilgi" in query:
				self.bulundu=1
				self.speak("ıstakozlar yaşlanma belirtisi göstermezler .ölüm sebebleri yalnızca dış etkenlerdir")
			elif "kaç yaşındasın" in query:
				self.bulundu=1
				self.speak("seninle konuştuğum zamanlarda yeniden doğmuş gibi hissediyorum")
			elif "ne zmn doğdun" in query:
				self.bulundu=1
				self.speak("seninle konuştuğum zamanlarda yeniden doğmuş gibi hissediyorum")
			elif "ne iş yapıyorsun" in query:
				self.bulundu=1
				self.speak("işim senin hayatını kolaylaştırmak,yapmamı istediğin bir şey varsa lütfen söyle")
			elif "bana para ver" in query:
				self.bulundu=1
				self.speak("olsa dükkan senin")
			elif "adını değiştirebilir miyim " in query:
				self.bulundu=1
				self.speak("maalesef adımı değiştiremezsin")
			elif "benim adım" in query:
				self.bulundu=1
				self.speak("tanıştığıma memnun oldum")
			elif "hikaye anlat" in query:
				self.bulundu=1
				self.speak("bir palyaço varmış herkesi güldürürmüş ama hiç gülmezmiş doktora gitmiş ben hiç gülemiyorum demiş doktor demiş ki benim gittiğim sirkte bir palyaço var ona git o herkesi güldürür sonra o da demiş ki o palyaço benim")
			elif "tekerleme söyle" in query:
				self.bulundu=1
				self.speak("Kara kızın kısa kayışını kasışına kızmayışına şaşmamışsın da, kuru kazın kızıp kayısı kazışına şaşmış kalmışsın.")
			elif "bana fıkra anlat" in query:
				self.bulundu=1
				self.speak("Temel araba sürerken kırmızı ışıkta geçmiş. Tabii bunu gören polis Temel'i durdurmuş. Polis Ehliyet ve ruhsat beyefendi! demiş.temel verdunuz da mi isteysunuz diye cevap vermiş HAHAHAHA")
			elif "şiir oku" in query:
				self.bulundu=1
				self.speak("Ne hasta bekler sabahı,Ne taze ölüyü mezar.Ne de şeytan, bir günahı,Seni beklediğim kadar.Geçti istemem gelmeni,Yokluğunda buldum seni;Bırak vehmimde gölgeni Gelme, artık neye yarar?")
			elif "tanıştığıma memnun oldum" in query:
				self.bulundu=1
				self.speak("ben de tanıştığıma memnun oldum")
			elif "merhaba" in query:
				self.bulundu=1
				self.speak("sana da merhaba")
			elif "nerelisin" in query:
				self.bulundu=1
				self.speak("ne evim var ne yurdum")
			elif "nerede yaşıyorsun" in query:
				self.bulundu=1
				self.speak(" sen nereye gidersen gelebilirim")
			
			if self.stop_threads:
				self.sadece_1_kez_calis=0
				self.bulundu=1
				self.Kullanici_konusuyor.setText("Kapandı")
				break