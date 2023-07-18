#import pyautogui
from PIL import ImageGrab
import cv2
import time
import numpy as np # numpy 패키지 로드하여 np로 사용

from tkinter import *

tk = Tk()
x = 0
y = 0
max_height = tk.winfo_screenheight()
max_width = tk.winfo_screenwidth()

FONT_PATH = "NanumSquareNeo-Variable.ttf"

#ocr원본 언어 설정
#import pytesseract as tract
#pytesseract.image_to_string(rgb_image, lang='en')
import easyocr
eocr = easyocr.Reader(['en'])

from translate import Translator
translator = Translator(from_lang="en", to_lang="ko")

def onChange(x):
  pass
#onChange(x) : E



# 캡쳐 시작 좌표, 가로, 세로 길이
x, y, width, height = 0, 0, 800, 500


#cv2컨트롤러 : S
cv2.namedWindow('edge detection', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname='edge detection', width=400, height=400)

cv2.createTrackbar('on', 'edge detection', 0, 1, onChange)
cv2.setTrackbarMin('on', 'edge detection', 0)
cv2.createTrackbar('x', 'edge detection', 0, max_width, onChange)
cv2.setTrackbarMin('x', 'edge detection', 0)
cv2.createTrackbar('y', 'edge detection', 0, max_height, onChange)
cv2.setTrackbarMin('y', 'edge detection', 0)
cv2.createTrackbar('width', 'edge detection', 1, max_width, onChange)
cv2.setTrackbarMin('width', 'edge detection', 1)
cv2.createTrackbar('height', 'edge detection', 1, max_height, onChange)
cv2.setTrackbarMin('height', 'edge detection', 1)
#cv2컨트롤러 : E

#im = pyautogui.screenshot(region=(0, 0, 10, 10))
im = ImageGrab.grab(bbox=(0, 0, 10, 10))
before = cv2.cvtColor(np.array(im), cv2.IMREAD_COLOR)
before = np.mean(im, axis=(0, 1))
while True:
  #캐니 엣지 값
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break  

  x = cv2.getTrackbarPos('x', 'edge detection')
  y = cv2.getTrackbarPos('y', 'edge detection')
  width = cv2.getTrackbarPos('width', 'edge detection')
  height = cv2.getTrackbarPos('height', 'edge detection')
  #im = pyautogui.screenshot(region=(x, y, width, height))
  im = ImageGrab.grab(bbox=(x, y, x + width, y + height))
  
  # 그레이 스케일로 변환
  src = cv2.cvtColor(np.array(im), cv2.IMREAD_COLOR)
  
  if 1 == cv2.getTrackbarPos('on', 'edge detection') :
    after = np.mean(im, axis=(0, 1))
    
    # TEST 2: Based on color of image
    if not (before[0] == after[0] and before[1] == after[1] and before[2] == after[2]):
      ocr_result = eocr.readtext(src) #([[36, 2], [110, 2], [110, 26], [36, 26]], 'import', 0.999067978196543)
      final_text = ''
      for sub_result in ocr_result: 
        final_text += sub_result[1]
      
      print(final_text)
      final_text = translator.translate(final_text)
      print(final_text)
      before = after

  cv2.imshow("edge detection", src)
  
1
cv2.destroyAllWindows()