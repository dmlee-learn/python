pip 문제시 복구
    다운 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    
    실행 python get-pip.py

# yolo
YOLO (You Only Look Once)는 실시간 객체 탐지를 위한 딥러닝 모델입니다. 

YOLO 모델을 사용하면 이미지나 비디오에서 객체를 탐지할 수 있습니다. 

YOLOv5는 PyTorch로 구현되어 있으며, 사용하기 편리합니다.

pip install ultralytics

# PIL
(Python Imaging Library)은 Python에서 이미지 처리 작업을 쉽게 수행할 수 있도록 도와주는 라이브러리입니다. Pillow는 PIL의 개선 버전으로, 현재는 Pillow 라이브러리를 사용하여 이미지를 처리합니다.

pip install Pillow

# ocr 
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

# 바코드
pip install pyzbar opencv-python

# 번역기
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
