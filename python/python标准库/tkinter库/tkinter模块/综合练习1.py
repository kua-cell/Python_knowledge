import tkinter as tkinter
from tkinter import messagebox


def on_button_click1():
   messagebox.showinfo("messagebox", "傻鸟，我是你爸爸！")
   # simpledialog.askstring("simpledialog", "傻鸟，我是你爸爸！")   

def on_button_click2():
    messagebox.showinfo("messagebox", "傻鸟，我本来只想当你爹，你却想让我当你爷，真是太好了！")
    # simpledialog.askstring("simpledialog", "傻鸟，我本来只想当你爹，你却想让我当你爷，真是太好了！")

# 创建窗口对象
window = tkinter.Tk()
window.geometry('150x300')

# 创建标签组件
label = tkinter.Label(window, text="现在，给你两个选择，来确定你我之间的关系：")

label.pack(expand="yes")

# 创建按钮组件;
frame1 = tkinter.LabelFrame(window, bg="blue", width=200, height=100)
frame1.pack(fill="both", expand=True)
button1 = tkinter.Button(frame1, text="A", command=on_button_click1, bg="red") 
button1.pack()

frame2 = tkinter.Frame(window, bg="blue", width=200, height=100)
frame2.pack(fill="both", expand=True)
button2 = tkinter.Button(frame2, text="B", command=on_button_click2, bg="red") 
button2.pack()

# 运行主循环
window.mainloop()