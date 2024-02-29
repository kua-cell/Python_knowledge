"""Python 断言是什么

Python 断言，即 Python assert 语句，简单理解就是简易版的 if 语句，
用于判断某个表达式的值，结果为 True，程序运行，否则，程序停止运行，抛出 AssertionError 错误。

语法格式如下所示：

assert 表达式

类比 if 语句，如下所示：

if not 表达式:
    raise AssertionError

在 assert 表达式之后，可以增加一个参数 [, arguments]，等价的 if 语句如下所示：

if not 表达式:
    raise AssertionError(arguments)

怎么用
模拟场景

在游戏里面设置一个未满 18 岁禁止访问的功能。
"""


def overage18(age):
    """

    Parameters
    ----------
    age
    """
    assert age >= 18, "对不起未满18岁，无法进行游戏"
    print("享受欢乐游戏时光")


if __name__ == '__main__':
    overage18(15)

"""但是这个案例并不是一个完美的案例，因为断言是为了告知 开发人员 ，你写的程序发生异常了。
如果一个潜在错误在程序编写前就能考虑到，例如程序运行时网络中断，这个场景就不需要使用断言。

    断言主要为调试辅助而生，为的是程序自检，并不是为了处理错误，程序 BUG 还是要依赖 try… except 解决。

由于断言是给 开发人员看的，所以下述案例的断言是有效的。
"""


def something():
    """
    该函数执行了很多操作
    """
    my_list = []  # 声明了一个空列表
    # do something
    return my_list


def func():
    """调用 something 函数，基于结果实现某些逻辑"""
    ret = something()
    assert len(ret) == 18, "列表元素数量不对"
    # 完成某些操作


"""使用断言要注意：
不要用断言验证用户的输入，这是因为 python 通过命令行运行时，如果增加 -O 标识，断言就被全局禁止了，你的所有验证就都丢失了。
常用断言函数

    assertEqual(a,b,msg=msg)：判断两个值是否相等；
    assertNotEqual(a,b,msg=msg)：上一函数的反义；
    self.assertTrue(a,msg=none)：判断变量是否为 True；
    assertFalse(a,msg=none)：同上反义；
    assertIsNone(obj=‘’)：判断 obj 是否为空；
    assertIsNotNone(obj=‘’)：同上反义；

还有其它函数，你可以任意检索资料，极容易掌握相关用法。
"""
"""扩展知识
Python 断言的适用场景

进行防御性的编程
我们在使用断言的时候，应该捕捉不应该发生的非法情况。这里要注意非法情况与异常错误之间的区别，
后者是必然存在的并且是一定要作出处理的。而断言后的条件不一定发生。

对假定条件做验证
断言是对程序员的假定做验证，因此这些假定的异常不一定会触发。
"""
