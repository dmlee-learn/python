pip 문제시 복구
    다운 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    실행 python get-pip.py


#ocr 
install pip install -q paddlepaddle paddleocr
pip install paddlepaddle paddleocr
apt-get install --reinstall python3-wget
    ocr 테스트
    !paddleocr --image_dir.jpg --lang=korean
혹은
pip install pytesseract
pip install pytesseract opencv-python

혹은
pip install easyocr

#바코드
pip install pyzbar opencv-python

#번역기
pip install googletrans==4.0.0-rc1
: import googletrans
  translator = googletrans.Translator()
  translator.translate(final_text, dest='ko').text 

pip install translate
: from translate import Translator
  translator = Translator(from_lang="en", to_lang="ko")
  text_en = translator.translate(r[4])

  
DBSCAN 을 위한 사이킷런 설치
pip install scikit-learn

# YOLOv5 저장소를 클론합니다.
git clone https://github.com/ultralytics/yolov5
cd yolov5

# 필요한 라이브러리를 설치합니다.
pip install -r requirements.txt

pip install Pillow==9.4.0   
