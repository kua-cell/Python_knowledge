# button组件

按钮(Button)

按钮组件用于在应用程序中添加按钮。按钮上可以显示文本或图像，并且可以与一个回调函数关联，当用户点击按钮时，自动调用该回调函数。

下面是一个简单的例子，它创建了一个按钮，并在用户点击按钮时弹出一个消息框：

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

上面的代码中，我们定义了一个回调函数on_button_click()，并在创建按钮组件时使用command参数将其与按钮关联。当用户点击按钮时，自动调用该回调函数。

运行上面的代码后，会弹出一个窗口，其中包含一个按钮。当用户点击该按钮时，会弹出一个消息框。
