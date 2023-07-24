import win32gui
class draw:
    hwnd = 0
    def __init__(self):
        pass

    def callback(self, _hwnd, _result: list):
        title = win32gui.GetWindowText(_hwnd)
        if win32gui.IsWindowEnabled(_hwnd) and win32gui.IsWindowVisible(_hwnd) and title is not None and len(title) > 0:
            _result.append(_hwnd)
        return True
    
    def getWindowHwndList(self):
        result = []
        win32gui.EnumWindows(self.callback, result)
        return result
    
    def getWindowList(self):
        hwnd_list = self.getWindowHwndList()

        windowList = {}
        index = 0
        for hwnd in hwnd_list:
            #가져온 hwnd 데이터를 이용해서 윈도우 창 이름을 가져와서 dictionary 추가
            windowList[hwnd] = win32gui.GetWindowText(hwnd)
            

        return windowList

app = draw()
list = app.getWindowList()
for key in list:
    print(str(key) + " : " + list[key])