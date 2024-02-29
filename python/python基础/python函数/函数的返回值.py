# 函数的返回值：
def add(x, y):
    result = x + y
    return result


# 函数的文件说明：
def func(x, y):
    """
    :param x: 参数x的说明
    :param y: 参数y的说明
    :return:  参数return的说明
    """
    result: object = x + y
    print(f"两数相加结果是：{result}")
    return result


func(5, 6)


# 还输的嵌套调用（一个函数里又调用一个函数）：
def func_b():
    print("---2---")


def func_a():
    print("---1---")

    func_b()

    print("---3---")


# 调用函数func_a
func_a()


# 函数的作用范围（作用域）：
# （1）局部变量 （2）全局变量
# eg：
def test_a():
    num = 100
    print(num)


test_a()  # 100.出了函数体，局部变量就会无法使用。
# print(num)  # 报错： name ‘num’ is not defined


# 演示全局变量:
num = 200


def testA():
    print(num)


def testB():
    num = 200
    print(num)


testA()  # 结果为100
testB()  # 结果为200
print(f'全局变量num={num}')  # 结果：全局变量num = 100
# 内部函数所定义的num属于局部变量，与开始定义的num（全局变量）无关（当内部变量发生改变，程序所输出的结果不受外部全局变量的影响）

# 出现以上情况需要用到global关键字，在函数内部声明变量为全局变量：
num = 100


def testA():
    print(num)


def testB():
    # global 关键字声明a是全局变量
    global num  # 设置内部变量为为全局变量
    num = 200
    print(num)


testA()  # 结果为100
testB()  # 结果为200
print(f'全局变量num={num}')  # 结果：全局变量num = 100
