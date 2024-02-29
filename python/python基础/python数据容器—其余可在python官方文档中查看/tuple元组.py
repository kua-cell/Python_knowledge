# 元组
# 定义元组
t1 = (1, "hello", True)
t2 = ()
t3 = tuple()
# 定义一个元素的元组
t4 = ("hello")
print(f"t4的类型为{type(t4)}, 其内容为：{t4}")
# 元组的嵌套与list相似
# 查找（下标索引取出内容）元组中的某一元素与list相同
# index查找方法：
t5 = ("itheima", "itcast", "python")
# 查找某元素在列表内的下标索引
index = t5.index("itheima")
print(f"itheima在元组内的下标索引值是：{index}")
#  统元组中某元素的数量{语法格式： 元组.count()}
t5 = ["itheima", "itcast", "python"]
count = t5.count("itheima")
print(f"元组中有{count}个'itheima'")
# len函数统计元组元素数量
t6 = ("itheima", "黑马程序员", "黑马程序员", "黑马程序员", "python")
num = len(t6)
print(f"元组t6中有几个元素：{num}")