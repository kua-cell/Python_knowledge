import tkinter as tk

# 创建窗口对象
window = tk.Tk()

# 创建画布组件
canvas = tk.Canvas(window, width=300, height=200)
canvas.pack()

# 绘制直线
canvas.create_line(0, 0, 300, 200, fill="red")

# 绘制矩形
canvas.create_rectangle(50, 50, 250, 150, fill="blue")

# 绘制文本
canvas.create_text(150, 100, text="Hello, Tkinter!", fill="white")

# 运行主循环
window.mainloop()
