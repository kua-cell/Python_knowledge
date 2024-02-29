import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Message", "Hello, Tkinter!")

# 创建窗口对象

window = tk.Tk()

# 创建按钮组件

button = tk.Button(window, text="Click me!", command=on_button_click)
button.pack()

# 运行主循环

window.mainloop()