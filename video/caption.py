import pyautogui
import cv2
import numpy as np # numpy 패키지 로드하여 np로 사용

# 캡쳐 시작 좌표, 가로, 세로 길이
x, y, width, height = 975, 170, 915, 400
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
org=(50,100)
font=cv2.FONT_HERSHEY_SIMPLEX
while True:
  im = pyautogui.screenshot(region=(x, y, width, height))
  # 그레이 스케일로 변환
  gray = cv2.cvtColor(np.array(im), cv2.COLOR_BGR2GRAY)
  
  # 캐니 엣지 검출
  edges = cv2.Canny(gray, 50, 150)
  
  # 허프 변환
  lines = cv2.HoughLinesP(edges, rho, theta, threshold, minLineLength, maxLineGap)

  # 검출된 도로 출력
  for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 2)
  
  text = f"threshold : {threshold}"
  
  cv2.putText(gray,text,org,font,1,(255,0,0),2)

  cv2.imshow("Screenshot", gray)
  """
  rho = 1
  theta = np.pi/180
  threshold = 300
  minLineLength = 20
  maxLineGap = 300
  """
  if cv2.waitKey(5) & 0xFF == ord('q'):
    break
  
  if cv2.waitKey(1) == ord('w'):
    threshold = treshold + 5
  if cv2.waitKey(1) == ord('s'):
    threshold = threshold - 5
  