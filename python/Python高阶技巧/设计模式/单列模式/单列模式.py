
# 非单列模式：
class Tool:
    pass


t1 = Tool()
t2 = Tool()
print(t1)
print(t2)

"""
创建类的实例后，就可以得到一个完整的、独立的类的对象。
通过print语句可以看出，他们的内存地址不同，即t1和t2是完全独立的两个对象。
<__main__.Tool object at 0x000001E9E24B2B10>
<__main__.Tool object at 0x000001E9E24B1970>

某些场景下，我们需要一个类，无论获取多少次类对象，都仅仅提供一个具体的实例
用以节省创建类对象的开销和内存开销
比如某些工具类，仅需1个实例，即可在各处使用

这就是单列模式所要实现的效果 
"""

"""
单列模式:  一种常用的软件设计模式，该模式的主要目的是确保某一个类只是一个实例存在。

在整个系统中，某个类只能出现一个实例时，单列模式就能派上用场。
·定义： 保证一个类只有一个实例，并提供一个访问它的全局访问点。
·适用场景：当一个类只能有一个实例，而客户可以从一个众所周知的访问点访问它时

"""


# 单列模式：
# class StrTools:
#    pass


# str_tools = StrTools()      # 在一个文件中定义如上代码

# from test import str_tools
#
# s1 = str_tools
# s2 = str_tools
# print(s1)
# print(s2)             # 在另一个文件中导入对象

"""
输出结果：
<test.StrTools object at 0x000001BB6FAEEE70>
<test.StrTools object at 0x000001BB6FAEEE70>

即s1和s2是同一个对象
"""
