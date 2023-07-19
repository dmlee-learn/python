#! /usr/bin/env python3
 
from tkinter import *
from tkinter import ttk
 
class Picture:
    def __init__(self, parent):
        self.parent = parent
        img = PhotoImage(file='c:/Users/siwon/OneDrive/document/GitHub/python/gui/test/iu.png')
        self.label = ttk.Label(self.parent)
        self.label['image'] = img
        img.image = img
        self.label.pack()
 
        btn = Button(self.parent, command=self.update, text='Test').pack(side='bottom', pady=50)
 
    def update(self):
        img = PhotoImage(file='c:/Users/siwon/OneDrive/document/GitHub/python/gui/test/suji.png')
        self.label['image'] = img
        img.image = img
 
def main():
    root = Tk()
    root.geometry('400x400+50+50')
    Picture(root)
    root.mainloop()
 
main()