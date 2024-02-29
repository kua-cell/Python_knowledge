import tkinter as tk

def on_checkbutton_click():
    print(var1.get(), var2.get())

# 创建窗口对象
window = tk.Tk()

# 创建布尔变量
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()

# 创建复选按钮组件
checkbutton1 = tk.Checkbutton(window, text="Option 1", variable=var1, command=on_checkbutton_click)
checkbutton1.pack()

checkbutton2 = tk.Checkbutton(window, text="Option 2", variable=var2, command=on_checkbutton_click)
checkbutton2.pack()

# 运行主循环
window.mainloop()