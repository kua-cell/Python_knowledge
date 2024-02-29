""""""
"""
list列表
一、查询功能
列表.index(元素)
"""
mylist = ["itheima", "itcast", "python"]

"""1.1 查找某元素在列表内的下标索引"""

index = mylist.index("itheima")
print(f"itheima在列表内的下标索引值是：{index}")

"""
# 1.2 如果被查找的元素不存在，会报错。
# index = mylist.index("hello")
# print(f"hello在列表内的下标索引值是：{index}")
"""

"""2. 修改特定下标索引的值"""

mylist[0] = "传智教育"
print(f"列表被修改元素后，结果是：{mylist}")

"""3.在指定下标位置插入新的元素"""

mylist.insert(1, "best")
print(f"指定下标位置插入新的元素后的列表内容为：{mylist}")

"""4.在列表的尾部追加‘’‘单个’‘’新元素"""

mylist.append("黑马程序员")
print(f"列表被追加元素结果：{mylist}")

""" 5.在列表的尾部追加‘’‘一批’‘’新元素"""

mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(f"追加一个新的列表后，结果为：{mylist}")

""" 6. 删除指定下标索引的元素（两种方式）"""

"""6.1 方式1： del 列表[下标]"""

del mylist[2]
print(f"列表删除元素后的结果为：{mylist}")

"""6.2 方式2： 列表.pop(下标)"""

element = mylist.pop(2)
print(f"通过pop方式删除列表元素后的结果为：{mylist}")

"""7. 删除指定下标索引的元素  列表.remove(元素)"""

mylist.remove("best")
print(f"通过remove方法移除元素后，列表结果为：{mylist}")

""""8. 清空列表"""

mylist.clear()
print(f"列表清空后，结果为:{mylist}")

"""9. 统计列表中某元素的数量  列表.count()"""

mylist = ["itheima", "itcast", "python"]
count = mylist.count("itheima")
print(f"列表中有{count}个'itheima'")

"""二、列表的遍历-while 循环："""


def list_while_func():
    """
    while循环遍历列表的演示函数
    ：return:None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    """
    # 循环控制变量通过下标索引来控制
    # 每次循环将下标索引变量+1
    # 循环条件：下标索引变量<列表的元素数量

    # 定义一个变量用来标记列表的下标
    """
    index = 0  # 初始值（即下标索引）为0

    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")
        # 至关重要，，，将循环变量（index）每次循环都加1
        index += 1


list_while_func()


def list_for_func():
    my_list: list[int] = [1, 2, 3, 4]
    # for 临时变量 in 数据容器

    for element in my_list:
        print(f"列表中的元素：{element}")


list_for_func()
