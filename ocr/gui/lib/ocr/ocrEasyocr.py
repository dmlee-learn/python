"""
try :
    from lib.ocr.baseocr import baseocr
except Exception as e:
    print(e)
    import baseocr
"""
import easyocr

class ocrEasyocr():
    #원본 언어 설정 영어 인식
    ocr = easyocr.Reader(['en'])
    #cls 는 글자가 회전 되어 있을 때 인식 하는 것 설정
    cls=False

    def __init__(self):
        self.ocr = easyocr.Reader(['en'])

    def setCls(self, cls):
        self.cls = cls

    def getTextFromImage(self, img):
        ocr_result = self.ocr.readtext(img)

        resultText = ''
        for sub_result in ocr_result: 
            resultText += " " + sub_result[1]
            
        return resultText 