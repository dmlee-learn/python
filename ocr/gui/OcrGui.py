# 모듈 호출
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image # Pillow
import threading
import numpy as np
#import easyocr

#ocr 인식 언어
#eocr = easyocr.Reader(['en'])

#ocr원본 언어 설정
#from paddleocr import PaddleOCR, draw_ocr
#원본 언어 설정 한국어 korean
#ocr = PaddleOCR(lang="en")

#번역기 영어 -> 한글
from translate import Translator
translator = Translator(from_lang="en", to_lang="ko")

#tk 설정
tkObject = Tk()
tkObject.title("GUI") #제목 설정
tkObject.geometry("920x640+50+50")#화면 크기
tkObject.resizable(False, False) #x축 ,y 축 리사이즈 방지

mainFrame = ttk.Frame(tkObject, padding=10)
#mainFrame.grid(row=0, column=0) # Frame : windows에서 새창이라는 느낌
mainFrame.pack(side="top", fill="both", expand=True) # Frame : windows에서 새창이라는 느낌
ttk.Label(mainFrame, text="Hello World!").grid(row=0, column=0) #라벨 주가 및 위치 설정

#tk 종료 버튼 클릭시 스레드 종료를 위한 변수
running = False
def exiting():
    print("exiting")
    global running
    running = False
    tkObject.destroy()
ttk.Button(mainFrame, text="Quit", command=exiting).grid(row=0, column=2) #종료 버튼 생성 및 위치 설정 


#캡쳐 클래스 활용 하여 캡쳐
from CaptureHelp import CaptureHelp
cap = CaptureHelp()

x=0
y=0
width=100
height=100
max_height = tkObject.winfo_screenheight()
max_width = tkObject.winfo_screenwidth()

cap.setCaptureBox(x, y, width, height)

before = False
def captureToImage():
    global before
    capimag = cap.capture()
    before = np.mean(capimag, axis=(0, 1))
    capimag = cap.imageProcessing(CaptureImage=capimag)      
    imageFormArray = Image.fromarray(capimag)
    transImage = ImageTk.PhotoImage(image=imageFormArray)
    
    return transImage;

from lib.ocr import ocrEasyocr
eocr = ocrEasyocr.ocrEasyocr()
def ocrRun(capimag):
    global eocr
    ocr_result = eocr.getTextFromImage(capimag)    
    return ocr_result

from lib.draw import draw
drawObj = draw.draw()

#def drawText(transText):
#    print("draw start") 
# #    drawObj.drawText(transText)



photo2 = captureToImage()

subFrame = ttk.Frame(tkObject, padding=10)
subFrame.pack(side="bottom", fill="both", expand=True) 
labelImage = ttk.Label(subFrame, image=photo2) #라벨 주가 및 위치 설정
#labelImage.grid(row=3, column=0) 
labelImage.pack()
def captureRun():
    print("captureRun start") 
    global running, cap, before

    while running:
        #drawObj.eleserText()
        capimag = cap.capture()
        #drawObj.restoreTExt()
        # 이미지의 rgb 값을 비교하여 같은 이미지 일경우 문자 인식 단계를 넘김
        after = np.mean(capimag, axis=(0, 1))
        if not (before[0] == after[0] and before[1] == after[1] and before[2] == after[2]):
            capimag = cap.imageProcessing(CaptureImage=capimag)          
            imageFormArray = Image.fromarray(capimag)
            imgtk = ImageTk.PhotoImage(image=imageFormArray)
            labelImage['image'] = imgtk
            before = after
            resultText = ocrRun(capimag)
            print(resultText)
            transText = translator.translate(resultText)
            print(transText) #번역후
            #drawObj.drawText(transText)


        

def startCapture():
    global running
    if running == True:
         running = False
    else :
        running = True
        thred = threading.Thread(target=captureRun)
        thred.start()

ttk.Button(mainFrame, text="imageChange", command=startCapture).grid(row=0, column=1) #종료 버튼 생성 및 위치 설정 



def selectX(var):
    var = int(float(var))
    global x
    x = var
    setCaptureBox()

def selectY(var):
    var = int(float(var))
    global y
    y = var
    setCaptureBox()

def selectWidth(var):
    var = int(float(var))
    global width 
    width = var
    setCaptureBox()

def selectHeight(var):
    var = int(float(var))
    global height
    height = var
    setCaptureBox()

def setCaptureBox():
    global cap    
    cap.setCaptureBox(x, y, x+width, y+height)
    drawObj.setRect(x, y, x+width, y+height)
        
        

ttk.Label(mainFrame, text="X").grid(row=1, column=0) #라벨 주가 및 위치 설정
textboxX = ttk.Scale(mainFrame,length=300, from_=0, to=max_width, orient='horizontal', command=selectX, variable=tk.IntVar())
textboxX.grid(row=1, column=1)
ttk.Label(mainFrame, text="Y").grid(row=1, column=2) #라벨 주가 및 위치 설정
textboxY = ttk.Scale(mainFrame, length=300, from_=0, to=max_height, orient='horizontal', command=selectY, variable=tk.IntVar())
textboxY.grid(row=1, column=3)
ttk.Label(mainFrame, text="Width").grid(row=2, column=0) #라벨 주가 및 위치 설정
textboxWidth = ttk.Scale(mainFrame, length=300, from_=1, to=max_width, orient='horizontal', command=selectWidth, variable=tk.IntVar())
textboxWidth.grid(row=2, column=1)
ttk.Label(mainFrame, text="Height").grid(row=2, column=2) #라벨 주가 및 위치 설정
textboxHeight = ttk.Scale(mainFrame, length=300, from_=1, to=max_height, orient='horizontal', command=selectHeight, variable=tk.IntVar())
textboxHeight.grid(row=2, column=3)

tkObject.mainloop() #GUI 루프 실행