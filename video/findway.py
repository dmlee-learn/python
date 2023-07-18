import pyautogui
import cv2
import math
import numpy as np # numpy 패키지 로드하여 np로 사용

def onChange(x):
  pass
#onChange(x) : E

#차선 인식 구역을 줄이기
def region_of_interrest(img):
  imshape = img.shape

  #ㅈ
  vertices = np.array([[
    (0, imshape[0])
    , (350, 180)
    , (500, 180)
    , (imshape[1]-20, imshape[0])]], dtype=np.int32)
    
  #defind a blank mask to start with
  mask = np.zeros_like(img)

  if len(img.shape) > 2:
    channel_count = img.shape[2]
    ignore_mask_color=(255,) * channel_count
  else:
    ignore_mask_color = 255

  cv2.fillPoly(mask, vertices, ignore_mask_color)

  #returning the image only where mask pixels are nonzero
  masked_image = cv2.bitwise_and(img, mask)
  return masked_image
#region_of_interrest

# 캡쳐 시작 좌표, 가로, 세로 길이
x, y, width, height = 985, 195, 890, 400
"""
image : 8bit, single-channel binary image, canny edge를 선 적용.
rho : r 값의 범위 (0 ~ 1 실수)
theta : 𝜃 값의 범위(0 ~ 180 정수)
threshold : 만나는 점의 기준, 숫자가 작으면 많은 선이 검출되지만 정확도가 떨어지고, 숫자가 크면 정확도가 올라감.
minLineLength : 선의 최소 길이. 이 값보다 작으면 reject.
maxLineGap : 선과 선사이의 최대 허용간격. 이 값보다 작으며 reject.
"""
rho = 1
theta = np.pi/180
threshold = 300
minLineLength = 20
maxLineGap = 300

#cv2컨트롤러 : S
cv2.namedWindow('edge detection')
cv2.createTrackbar('low threshold', 'edge detection', 0, 255, onChange)
cv2.setTrackbarMin('low threshold', 'edge detection', 10)
cv2.createTrackbar('high threshold', 'edge detection', 0, 255, onChange)
cv2.setTrackbarMin('high threshold', 'edge detection', 10)
cv2.createTrackbar('hup threshold', 'edge detection', 0, 500, onChange)
cv2.setTrackbarMin('hup threshold', 'edge detection', 10)
#cv2컨트롤러 : E

while True:
  #캐니 엣지 값
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
    
  low = cv2.getTrackbarPos('low threshold', 'edge detection')
  high = cv2.getTrackbarPos('high threshold', 'edge detection')
  hup_threshold = cv2.getTrackbarPos('hup threshold', 'edge detection')

  im = pyautogui.screenshot(region=(x, y, width, height))
  # 그레이 스케일로 변환
  src = cv2.cvtColor(np.array(im), cv2.IMREAD_COLOR)
  gray = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2GRAY)
  
  # 캐니 엣지 검출
  edges = cv2.Canny(gray, low, high)

  mask = region_of_interrest(edges)
  
  # 허프 변환
  #lines = cv2.HoughLinesP(mask, 1, np.pi/180, threshold, 20, maxLineGap=300)
  lines = cv2.HoughLinesP(mask, 1, np.pi/180, hup_threshold, None, 0, 0)

  # 검출된 도로 출력
  if lines is not None:
    for line in lines:
      x1, y1, x2, y2 = line[0]
      cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2)
      """
      rho = line[0][0]
      theta = line[0][1]
      a = math.cos(theta)
      b = math.sin(theta)
      x0 = a * rho
      y0 = b * rho
      pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
      pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
      cv2.line(gray, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
      """
      
  
  cv2.imshow("edge detection", src)

cv2.destroyAllWindows()