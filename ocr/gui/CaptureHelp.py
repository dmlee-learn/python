import cv2
from PIL import ImageGrab
import numpy as np


class CaptureHelp:
    
    def __init__(self):
        self.x=0
        self.y=0
        self.width=100
        self.height=100

    def getWidth():
        return self.width

    def setCaptureBox(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def capture(self):       
        #이미지 캡쳐
        CaptureImage = ImageGrab.grab(bbox=[self.x, self.y, self.width, self.height], all_screens=False)
        resultImage = self.imageProcessing(CaptureImage)
        return resultImage
    
    def imageProcessing(self, CaptureImage):

        """
        선 검출
        edge = cv2.Canny(src, 50, 150)

        투시변환
        입력 영상으로 사용한 영수증의 외곽선은 크기가 가장 큰 4개의 외곽선으로 이루어져 있다는 점을 이용해 외곽선을 크기순으로 정렬

        contours = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]  # 외곽선 크기순으로 정렬

        for i in contours:
            length = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * length, True)

            if len(approx) == 4:
                contourCnt = approx
                break

        # 투시변환
        src_pts = np.array([[approx[0][0][0], approx[0][0][1]],
                            [approx[1][0][0], approx[1][0][1]],
                            [approx[2][0][0], approx[2][0][1]],
                            [approx[3][0][0], approx[3][0][1]]]).astype(np.float32)

        w = 300
        h = 400

        dst_pts = np.array([[0, 0],
                            [0, h - 1],
                            [w - 1, h - 1],
                            [w - 1, 0]]).astype(np.float32)

        pers_mat = cv2.getPerspectiveTransform(src_pts, dst_pts)
        src_transform = cv2.warpPerspective(src, pers_mat, (w, h))
       

        
        
        """

        #흑백 변환
        CaptureGray = cv2.cvtColor(np.array(CaptureImage), cv2.COLOR_BGR2GRAY)

        #이진화
        _, CaptureBinary = cv2.threshold(np.array(CaptureGray), 0, 255, cv2.THRESH_OTSU)

        
        
        #에지 정보를 유지하며 노이즈을 효과적으로 제거하기 위해 양방향 필터 수행
        CaptureFiltering = cv2.bilateralFilter(CaptureBinary, -1, 10, 5)
        
        #모폴로지 연산
        #kernel = np.ones((3, 1), np.uint8)
        #src_morphology = cv2.morphologyEx(src_filtering, cv2.MORPH_OPEN, kernel)
        return CaptureFiltering

        