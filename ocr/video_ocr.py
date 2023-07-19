#import pyautogui
from PIL import ImageGrab
import cv2
import time
import numpy as np # numpy 패키지 로드하여 np로 사용

from tkinter import *

#모니터 해상도 확인
tk = Tk()
x = 0
y = 0
max_height = tk.winfo_screenheight()
max_width = tk.winfo_screenwidth()

#추후 화면에 한글을 적기 위하여 폰트 설정
FONT_PATH = "NanumSquareNeo-Variable.ttf"

#ocr원본 언어 설정
#import pytesseract as tract
#pytesseract.image_to_string(rgb_image, lang='en')
#ocr 리더기
import easyocr
eocr = easyocr.Reader(['en'])

#번역기
from translate import Translator
translator = Translator(from_lang="en", to_lang="ko")

def onChange(x):
  pass
#onChange(x) : E

# 캡쳐 시작 좌표, 가로, 세로 길이
x, y, width, height = 0, 0, 800, 500


#cv2컨트롤러 : S
cv2.namedWindow('text detection', flags=cv2.WINDOW_NORMAL)
cv2.resizeWindow(winname='text detection', width=400, height=400)

#cv 컨트롤러 캡쳐 온오프 x, y, width, mheight 캡쳐할 구역 선택
cv2.createTrackbar('on', 'text detection', 0, 1, onChange)
cv2.setTrackbarMin('on', 'text detection', 0)
cv2.createTrackbar('x', 'text detection', 0, max_width, onChange)
cv2.setTrackbarMin('x', 'text detection', 0)
cv2.createTrackbar('y', 'text detection', 0, max_height, onChange)
cv2.setTrackbarMin('y', 'text detection', 0)
cv2.createTrackbar('width', 'text detection', 1, max_width, onChange)
cv2.setTrackbarMin('width', 'text detection', 1)
cv2.createTrackbar('height', 'text detection', 1, max_height, onChange)
cv2.setTrackbarMin('height', 'text detection', 1)
#cv2컨트롤러 : E

#im = pyautogui.screenshot(region=(0, 0, 10, 10))
im = ImageGrab.grab(bbox=(0, 0, 10, 10))
before = cv2.cvtColor(np.array(im), cv2.IMREAD_COLOR)
before = np.mean(im, axis=(0, 1))

#추후 thread로 변경시 좀 더 좋을 것 같음
while True:
  #q키로 종료를 위한 추가 설정
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break  

  #캡쳐를 위한 구역 설정
  x = cv2.getTrackbarPos('x', 'text detection')
  y = cv2.getTrackbarPos('y', 'text detection')
  width = cv2.getTrackbarPos('width', 'text detection')
  height = cv2.getTrackbarPos('height', 'text detection')

  #화면 캡쳐 속도를 빠르게 하기 위하여 PIL라이브러리로 변경
  #im = pyautogui.screenshot(region=(x, y, width, height))
  im = ImageGrab.grab(bbox=(x, y, x + width, y + height))
  
  # 이미지를 easyocr로 인식 가능한 이미지로 컨버팅
  src = cv2.cvtColor(np.array(im), cv2.IMREAD_COLOR)
  
  if 1 == cv2.getTrackbarPos('on', 'text detection') :
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

  cv2.imshow("text detection", src)
  
cv2.destroyAllWindows()