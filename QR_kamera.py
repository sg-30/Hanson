
import cv2
from pyzbar import pyzbar
import numpy as np
import pyscreenshot
import pyautogui
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Qr_Kod():
    def __init__(self):
        self.tiklandi=False
        self.oku=False
        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.setWindowTitle("Unreadable Qr Error")

    def mousePoints(self,event,x,y,flags,params):#qr kodu ekrandan seçmemizi sağlar
        if(event==cv2.EVENT_LBUTTONDOWN):
            self.x1=x
            self.y1=y
            self.x2=x
            self.y2=y
            self.tiklandi=True
        elif(event==cv2.EVENT_MOUSEMOVE and self.tiklandi==True):
            self.x2=x
            self.y2=y
        elif(event==cv2.EVENT_LBUTTONUP):
            self.x2=x
            self.y2=y
            self.tiklandi=False
            self.imag=cv2.cvtColor(np.array(pyscreenshot.grab(bbox=(self.x1,self.y1,self.x2,self.y2))),cv2.COLOR_RGB2BGR)  
            self.read_barcodes(self.imag)
            if(self.oku==False):
                self.error_dialog.showMessage('Please check you Qr')
                cv2.destroyAllWindows()

        if self.tiklandi==True:
            self.ima = self.imag.copy()
            cv2.rectangle(self.ima, (self.x1, self.y1),(self.x2, self.y2), (0, 255, 0), 1)
            cv2.imshow("Qr_kod",self.ima) 

    def read_barcodes(self,frame):#barkod okur
        barcodes = pyzbar.decode(frame)
        
        for barcode in barcodes:
            x, y , w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y),(w+x, h+y), (0, 255, 0), 2)
            webbrowser.open(barcode_info)
            cv2.destroyAllWindows()
            break
        
        return frame

    def manuel(self):#programı alt taba alarak ss almak istediğimiz ekranı açar
        pyautogui.keyDown('alt')
        pyautogui.press("tab")
        pyautogui.keyUp("alt") 
        self.resim()

    def resim(self):#ekran fotoğrafı alıp qr kodu seçmemiz için mouse a yollar
        self.imag=cv2.cvtColor(np.array(pyscreenshot.grab()),cv2.COLOR_RGB2BGR)  
        
        self.ima = self.imag.copy()
        cv2.namedWindow("Qr_kod", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Qr_kod", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty("Qr_kod", cv2.WND_PROP_TOPMOST, 1)
        cv2.imshow("Qr_kod",self.ima) 
        cv2.setMouseCallback("Qr_kod",self.mousePoints)
        cv2.waitKey(0)

def Qr_resim_manuel():
    Qr_Kod().manuel()

def Qr_resim_otomatik():
    Qr_Kod().resim()