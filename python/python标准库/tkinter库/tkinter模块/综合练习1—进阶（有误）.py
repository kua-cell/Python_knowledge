import tkinter as tkinter

class selection:
    def __init__(self,master):
        self.master = master
        self.master.title("测试")

        self.result = tkinter
        # 创建标签组件
        self.result_label=tkinter.Label(self.master)
    def create_button(self):
        self.button1 = tkinter.Button(window, text="A") 
        self.button1.pack()
        self.button2 = tkinter.Button(window, text="B") 
        self.button2.pack()
    def on_button_click(self,text):        
        if text =="A":
            self.result.set("傻鸟，我是你爸爸！")
            return
        if text=="B":
            self.result.set("傻鸟，我本来只想当你爹，你却想让我当你爷，真是太好了！")

if __name__ == "__main__":
# 创建窗口对象
    window = tkinter.Tk()
    selection = selection(window)
# 运行主循环
    window.mainloop()