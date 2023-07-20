# 모듈 호출
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image # Pillow
import threading

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
cap.setCaptureBox(x, y, width, height)

def captureToImage():
    capimag = cap.capture()
    imageFormArray = Image.fromarray(capimag)
    transImage = ImageTk.PhotoImage(image=imageFormArray)
    return transImage;

def ocrRun():
    after = np.mean(im, axis=(0, 1))
    
    # 이미지의 rgb 값을 비교하여 같은 이미지 일경우 문자 인식 단계를 넘김
    if not (before[0] == after[0] and before[1] == after[1] and before[2] == after[2]):
      ocr_result = eocr.readtext(src) #([[36, 2], [110, 2], [110, 26], [36, 26]], 'import', 0.999067978196543)
      final_text = ''
      for sub_result in ocr_result: 
        final_text += sub_result[1]
      
      print(final_text) #번역전
      final_text = translator.translate(final_text)
      print(final_text) #번역후
      before = after

photo2 = captureToImage()

subFrame = ttk.Frame(tkObject, padding=10)
subFrame.pack(side="bottom", fill="both", expand=True) 
labelImage = ttk.Label(subFrame, image=photo2) #라벨 주가 및 위치 설정
#labelImage.grid(row=3, column=0) 
labelImage.pack()
def captureRun():
    print("captureRun start") 
    global running
    global cap
    while running:
        capimag = cap.capture()
        imageFormArray = Image.fromarray(capimag)
        imgtk = ImageTk.PhotoImage(image=imageFormArray)
        labelImage['image'] = imgtk

        

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
    global width 
    x = var
    width = var + width
    setCaptureBox()

def selectY(var):
    global y
    global height
    y = var
    height = var + height
    setCaptureBox()

def selectWidth(var):
    global x
    global width 
    width = var + x
    setCaptureBox()

def selectHeight(var):
    global y
    global height
    height = var + y
    setCaptureBox()

def setCaptureBox():
    global cap
    cap.setCaptureBox(x, y, width, height)
        
        

ttk.Label(mainFrame, text="X").grid(row=1, column=0) #라벨 주가 및 위치 설정
textboxX = ttk.Scale(mainFrame, from_=0, to=100, orient='horizontal', command=selectX, variable=tk.IntVar())
textboxX.grid(row=1, column=1)
ttk.Label(mainFrame, text="Y").grid(row=1, column=2) #라벨 주가 및 위치 설정
textboxY = ttk.Scale(mainFrame, from_=0, to=100, orient='horizontal', command=selectY, variable=tk.IntVar())
textboxY.grid(row=1, column=3)
ttk.Label(mainFrame, text="Width").grid(row=1, column=4) #라벨 주가 및 위치 설정
textboxWidth = ttk.Scale(mainFrame, from_=0, to=100, orient='horizontal', command=selectWidth, variable=tk.IntVar())
textboxWidth.grid(row=1, column=5)
ttk.Label(mainFrame, text="Height").grid(row=1, column=6) #라벨 주가 및 위치 설정
textboxHeight = ttk.Scale(mainFrame, from_=0, to=100, orient='horizontal', command=selectHeight, variable=tk.IntVar())
textboxHeight.grid(row=1, column=7)

tkObject.mainloop() #GUI 루프 실행