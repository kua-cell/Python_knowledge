import tkinter as tkinter

# 创建窗口对象
window = tkinter.Tk()

# 创建标签组件
label = tkinter.Label(window, text="hello,tkinter!")
label.pack()
label.grid(row=0, column=0)

# 创建按钮组件
button = tkinter.Button(window, text="点击此处进入") 
button.pack()
button.grid(row=1, column=1)

# 运行主循环
window.mainloop()