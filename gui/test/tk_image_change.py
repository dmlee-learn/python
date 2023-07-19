import tkinter as tk

root = tk.Tk()  # tkinter root창 생성

root.title("계산기") #창 이름
root.geometry("500x500+200+200") # 창 크기, 가로 x 세로 + 창 출력 위치 좌표

'''
글자 입력하기
'''
label1 = tk.Label(root, text="누굴까")
label1.pack()

'''
사진 입력하기
'''
photo = tk.PhotoImage(file="c:/Users/siwon/OneDrive/document/GitHub/python/gui/test/iu.png")
label2= tk.Label(root, image=photo)
label2.pack()

'''
버튼 클릭시 label1의 내용 변경시키기
'''
def change_a():
    label1.config(text="아이유 아이유!!")

button1 = tk.Button(root, text="클릭", command=change_a)
button1.pack()

'''
버튼 클릭시 label2의 사진 변경시키기
'''
def change_b():
    '''
    garbage collection 때문에 phto2는 global 선언
    '''
    global photo2
    photo2 = tk.PhotoImage(file="c:/Users/siwon/OneDrive/document/GitHub/python/gui/test/suji.png")
    label2.config(image=photo2)


button2 = tk.Button(root, text="아이유 사진 변경시키기", command=change_b)
button2.pack()

root.mainloop()

