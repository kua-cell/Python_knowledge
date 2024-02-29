"""
threading模块
绝大多数编程语言，都允许多线程编程，Python也不例外。
Python的多线程可以通过threading模块来实现。
"""
import threading
import time

# threading_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
"""
单线程：
def sing():
    while True:
        print("我在唱歌，啦啦啦")
        time.sleep(1)


def dance():
    while True:
        print("我在跳舞，呱呱呱")
        time.sleep(1)


if __name__=="__main__":
    sing()
    dance()

运行结果为：
我在唱歌，啦啦啦
我在唱歌，啦啦啦
我在唱歌，啦啦啦
我在唱歌，啦啦啦
我在唱歌，啦啦啦
我在唱歌，啦啦啦
我在唱歌，啦啦啦
。。。。
"""

# def sing():
#     while True:
#         print("我在唱歌，啦啦啦")
#         time.sleep(1)
#
#
# def dance():
#     while True:
#         print("我在跳舞，呱呱呱")
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     # 创建一个唱歌线程：
#     sing_threading = threading.Thread(target=sing)
#     # 创建一个跳舞线程：
#     dance_threading = threading.Thread(target=dance)
#
#     # 让线程去干活
#     sing_threading.start()
#     dance_threading.start()

"""
运行结果为：
我在唱歌，啦啦啦
我在跳舞，呱呱呱
我在唱歌，啦啦啦我在跳舞，呱呱呱

我在跳舞，呱呱呱我在唱歌，啦啦啦

......
"""


# 需要传参的话：
def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


# 如果不想让程序持续运行，可去掉while语句

if __name__ == "__main__":
    # 创建一个唱歌线程：
    sing_threading = threading.Thread(target=sing, args=("我在唱歌，啦啦啦",))
    # 创建一个跳舞线程：
    dance_threading = threading.Thread(target=dance, kwargs={"msg": "我在跳舞，呱呱呱"})

    # 让线程去干活
    sing_threading.start()
    dance_threading.start()
