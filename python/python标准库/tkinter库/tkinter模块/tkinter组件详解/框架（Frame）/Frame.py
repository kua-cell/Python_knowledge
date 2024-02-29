import tkinter as tk

# 创建窗口对象
window = tk.Tk()

# 创建框架1
frame1 = tk.Frame(window, bg="red", width=200, height=100)
frame1.pack(fill="both", expand=True)

# 在框架1中添加标签
label = tk.Label(frame1, text="Hello, Tkinter!")
label.pack()

# 创建框架2
frame2 = tk.Frame(window, bg="blue", width=200, height=100)
frame2.pack(fill="both", expand=True)

# 在框架2中添加按钮
button = tk.Button(frame2, text="Click me!")
button.pack()

# 运行主循环
window.mainloop()
