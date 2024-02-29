import tkinter as tk

def on_entry_change(sv):
    print(sv.get())

# 创建窗口对象
window = tk.Tk()

# 创建字符串变量
sv = tk.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: on_entry_change(sv))

# 创建条目组件
entry = tk.Entry(window, textvariable=sv)
entry.pack()

# 运行主循环
window.mainloop()
