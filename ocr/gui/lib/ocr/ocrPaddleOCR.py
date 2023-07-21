from baseocr import baseocr
from paddleocr import PaddleOCR, draw_ocr

class ocrEasyocr(baseocr):
    #원본 언어 설정 영어 인식
    ocr = PaddleOCR(lang="en")
    #cls 는 글자가 회전 되어 있을 때 인식 하는 것 설정
    cls=False

    def __init__(self):
        self.ocr = PaddleOCR(lang="en")

    def setCls(self, cls):
        self.cls = cls

    def getTextFromImage(self, img):
        textArray = self.ocr.ocr(img, self.cls) 
        return textArray 