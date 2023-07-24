import win32gui, win32api, win32con, win32ui
import time

class draw:
    x = 0
    y = 0
    width = 1 
    height = 1
    rect = (0,0,1,1)
    color = win32api.RGB(0,255,0)
    windowText = ''
    backupText = ''
    hwnd = 0
    hdc = ''

    def __init__(self):
        #데스크탑 윈도우의 하드웨어 값
        self.hwnd = win32gui.GetDesktopWindow()
        #device context
        self.hdc = win32gui.GetDC(self.hwnd)
        #self.hdc, paintStruct = win32gui.BeginPaint(self.hwnd)

        win32gui.GetDesktopWindow()
        print(" i ")
        print(win32gui.GetDesktopWindow())
        print(win32gui.GetDC(self.hwnd))
    
    def setRect(self, x, y, width, height, color=False):
        self.color = win32api.RGB(0,255,0) if not color else win32api.RGB(color[0], color[1], color[2])
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect=(self.x,self.y,self.width, self.height)
    """
    def rect(self, x, y, w, h, color=False):
        for i in range(x, x + w):
            win32gui.SetPixel(self.hdc, i, y, color)
            win32gui.SetPixel(self.hdc, i, y + h, color)
        for j in range(y, y + h):
            win32gui.SetPixel(self.hdc, x, j, color)
            win32gui.SetPixel(self.hdc, x + w, j, color)
    """

    def drawText(self, str):
        self.windowText = str

        # 폰트 만들기
        font_spec = {'name':'Arial', 'height':42, 'weight':30}
        font = win32ui.CreateFont(font_spec)
        oldfont = win32gui.SelectObject(self.hdc, font.GetSafeHandle())

        #글자를 화면에 그리는 함수 hdc로 추가 제어 가능
        win32gui.DrawText(self.hdc, str, -1, self.rect, win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_VCENTER)
            
    def eleserText(self): 
        try :            
            self.backupText = self.windowText
            self.windowText = " ㅇ ㅇ  ㅇ  ㅇ ㅇ ㅇ ㅇ ㅇㅇ"
            #화면에 그려진 것을 갱신 하는 함수
            #win32gui.RedrawWindow(self.hwnd, self.rect, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
            #win32gui.DrawText(self.hdc, self.windowText, -1, self.rect, win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_VCENTER)
            #win32gui.InvalidateRect(self.hwnd, None, True)
            win32gui.InvalidateRect(self.hwnd, None, True) 

            print(" e ")
            print(win32gui.GetDesktopWindow())
            print(win32gui.GetDC(self.hwnd))

            win32gui.ReleaseDC(self.hwnd, self.hdc)
            win32gui.DeleteDC(self.hdc)
            
        except Exception as ex:
            print(ex)

    def restoreTExt(self):
        try :            
            self.windowText = self.backupText
            time.sleep(1.0)
            win32gui.RedrawWindow(self.hwnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)            
        except :
            pass
        
#app = draw()
#app.setRect(20, 10, 400, 400)
#app.drawText("ddddd")
#app.eleserText()

# 빨간색으로 하려면 아래처럼
# app.rect(20, 10, 55, 55, (255,0,0))