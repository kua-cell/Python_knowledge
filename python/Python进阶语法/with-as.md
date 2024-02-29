# Python with…as…是什么

在 Python 中，文件操作，数据库操作，都需要在程序执行完毕进行清理工作，很多时候我们经常忘记手动关闭，因此 Python 集成了一种自动操作，例如文件使用自后，自动释放资源。

上述场景的描述，转换成 Python 语法就是 with...as 语句，即上下文管理器，它在 Python 中实现了自动分配并释放资源。

with…as 语句的语法格式如下

with 表达式 [as 指定一个变量名]:
	代码块
	代码块
其中 [] 中的内容可以省略，如果使用表示将前文表达式的结果保存到一个变量中。

怎么用
用于文件操作
with...as... 语句初次接触一般是在文件操作中，如果不使用上下文管理器，对一个文件进行操作的代码如下所示：

file = open("./demo.txt") # 手动打开
data = file.read()
file.close() # 手动关闭
下面是 with...as... 版本的代码：

with open("./demo.txt") as file:
    data = file.read()
如果不使用上述语句，想要完成一个完善的代码段，需要使用 try...except... 语句进行操作。

file = open("./demo.txt")
try:
    data = file.read()
finally:
    file.close()
提高场景 - with 工作原理
接下来通过自己实现一个支持上下文管理器的类，进一步了解 with...as... 的工作原理。

实现原理非常简单，要求在类中实现 __enter__ 和 __exit__ 两个方法即可。

例如我们编写一个动物类 Animal，然后增加上述两个方法。

class Animal:
    def __enter__(self):
        print("__enter__()")

    def __exit__(self, type, value, trace):
        print("__exit__()")


with Animal() as animal:
    pass
你也可以试一下，如果不编写上述两个方法，会出现什么异常。

异常为：AttributeError: __enter__

其中 __exit__() 方法有 3 个参数，这些参数用于异常处理，参数含义如下所示：

type：异常类；
value：异常值；
trace：调用栈信息。
当 with...as... 后的代码块抛出异常时，__exit__() 方法被执行，因此在 with 语法中的 __exit__ 方法中可以处理异常，并且不需要使用 try...except ，如果希望忽略异常，只需要在 __exit__ 方法中返回 True 即可，代码为 return True 。

扩展部分
有人说 with…as，是 python 控制流语句，有人说 with…as 是简化版的 try 语句，你觉得呢？
