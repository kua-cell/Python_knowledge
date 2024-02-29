"""
装饰器也是一种闭包
其在不破坏目标函数原有的代码和功能的前提下，为目标函数增加新功能
"""


# 一般写法（闭包写法）：
def outer(func):
    def inner():
        print("我要睡觉了！")
        func()
        print("我起床了!")

    return inner


def sleep():
    import random
    import time
    print("睡眠中。。。")
    time.sleep(random.randint(1, 6))


fn = outer(sleep)
fn()


# 装饰器的语法糖写法(快捷写法)：
# 使用@outer，定义在目标函数sleep之上
def outer(func):
    def inner():
        print("我要睡觉了！")
        func()
        print("我起床了！")

    return inner


@outer      # 自己的理解： 相当于将sleep函数定义为outer函数的成员属性
def sleep():
    import random
    import time
    print("睡眠中。。。")
    time.sleep(random.randint(1,6))


sleep()     # 不再像一般写法，写完后在调用函外部数



# 执行结果：
# 我要睡觉了
# 睡眠中。。。
# 我起床了！