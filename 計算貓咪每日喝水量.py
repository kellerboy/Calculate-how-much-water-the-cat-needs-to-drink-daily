
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from PIL import ImageTk, Image

def event1():
    global entry1
    global v
    global comboExample
    print(comboExample.current(), comboExample.get())
    t1=entry1.get()     ###取得用戶輸入的文字或數字
    weight=int(t1)
    comStr = comboExample.get()
    if comStr == "幼貓":
        water = weight *40
    elif comStr == "成貓":
        water = weight *70
    elif comStr == "老貓":
        water = weight *80
    v.set(str(water))
    print("每日喝水量",water,"CC")

win = tk.Tk()
win.wm_title("貓咪每日喝水量計算 ")
win.minsize(width=400, height=500)  #視窗最小SIZE
win.maxsize(width=400, height=500)  #視窗最大SIZE
win.resizable(width=False, height=False) # 是否可以改變視窗大小
img = ImageTk.PhotoImage(Image.open("cat10.jpg"))

background_image = ImageTk.PhotoImage(Image.open("cat3.jpg")) #背景圖片
background_label = tk.Label(win, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

op1 =tk.Button(win,text="請輸入貓咪體重(公斤)=",fg="blue",)
op1.place(x=10, y=20)
entry1=tk.Entry(win)
entry1.place(x=150, y=25)
btn1 =tk.Button(win,text="計算貓咪每日喝水量",image = img,command=event1)
btn1.place(x=10, y=100,)
op2 =tk.Button(win,text="貓咪每日喝水量為=",fg="blue",)
op2.place(x=10, y=360)
op3 =tk.Button(win,text="cc",fg="blue",)
op3.place(x=210, y=360)
v = StringVar()     #
label1 =tk.Label(win,textvariable=v,fg="red",)
label1.place(x=150, y=362)
v.set("顯示於此")

op2 =tk.Button(win,text="請選擇貓咪為",fg="blue",)
op2.place(x=10, y=60)
comboExample = ttk.Combobox(win,
                            values=[
                                    "幼貓",
                                    "成貓",
                                    "老貓",])
comboExample.place(x=100,y=62)
comboExample.current(1)
win.mainloop()



