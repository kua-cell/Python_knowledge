"""
列表推导式，python的一种特殊的数据处理方式，节省代码运行时间

推导式： 一种普通的语法定义词，可称之为  解析式

1. if条件表达式：
[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]]

@for循环写法："""
my_list = [1, 2, 3]
new_list = []
for i in my_list:
    new_list.append(i * 2)

print(new_list)
"""
列表推导式写法：
"""
nn_list = [i * 2 for i in my_list]  # for关键字是一个普通的循环，前面的表达式i*2其中的i就是for循环中的变量
print(nn_list)
"""
对比之下，比前者增加一个[]
注意最终各个结果会组成一个新的列表

if语句是一个判断，其中i也是前面循环产生的迭代变量
"""
nn_list = [i * 2 for i in my_list if i > 1]
print(nn_list)

"""可优化两层for循环"""
nn_list = [(x, y) for x in range(3) for y in range(3)]
print(nn_list)
"""
如果不想让别人看懂你的代码：
可以无限套娃————列表推导式没有循环层数限制
依旧支持if语句，if后可以用前面所有迭代产生的变量，不建议超过两成，会降低代码的可阅读性
"""
# 三层的列表推导式：
nn_list = [(x, y, z, m) for x in range(3) for y in range(3) for z in range(3) for m in range(3)]
print(nn_list)

"""列表推导式支持嵌套"""
# 如下代码：
my_var = [y*4 for y in [x * 2 for x in range(3)]]
print(my_var)

"""列表推导式可用于转换数据"""
my_list = [1, 2, 3]

new_list = [item * 2 for item in my_list]
print(new_list)             # item 是从my_list遍历而来

"""列表推导式也可用于过滤数据"""
my_list = [1, 2, 3]

new_list = [item * 2 for item in my_list if item > 1]
print(new_list)

"""字典推导式"""
# 语法格式：{键:值 for 迭代变量 in 可迭代变量[if 条件表达式]}
# 案例;
my_dict = {key: value for key in range(3) for value in range(2)}
print(my_dict)  # 运行结果为：{0: 1, 1: 1, 2: 1}
"""字典中不能出现同名的key，再次出现则会把第一个值覆盖掉，得到的value全是1"""
"""最常见的还是下述代码, 遍历一个具有键值关系的可迭代对象。"""
my_tuple_list = [('name', '橡皮擦'), ('age', 18), ('class', 'No1'), ('like', 'python')]
my_dict = {key: value for key, value in my_tuple_list}
print(my_dict)
# 运行结果：{'name': '橡皮擦', 'age': 18, 'class': 'No1', 'like': 'python'}

"""元组推导式与集合推导式"""
# 元组推导式与前几种语法差不多，但结果不同
my_tuple = (i for i in range(10))
print(my_tuple)  # 结果不是元组，而是一个生成器对象，也叫生成器语法
# 集合推导式：
my_set = {value for value in 'HelloWorld'}
print(my_set)
"""集合是无序且不重复的, 所以会自动去掉重复的元素，并且每次运行显示的顺序都不一样"""

"""
提高场景
再次查看推导式语法结构中，涉及了一个关键字，叫做 可迭代对象，因为我们可以把自己目前掌握的所有可迭代对象，
都进行一下尝试，例如使用 range() 函数。
"""

my_list = [1, 2, 3]
new_list = [item for item in range(1, 10) if item > 5]
print(new_list)
"""
检验是否掌握，可以回答下述两个问题。

如果可迭代对象是一个字典，你该如何操作？
如果可迭代对象位置使用了 enumerate() 函数，你该如何操作？
enumerate()函数是Python中一个非常实用的内建函数，它用于同时遍历序列中的元素及其下标。
该函数在for循环中使用时，它会返回一个迭代器，迭代器中的元素是一个元组，包含当前元素的值和其下标。
下面是enumerate()函数的基本用法：
for index, value in enumerate(sequence):
    print(index, value)

这里，sequence是你要遍历的序列，可以是列表、元组或字符串等。`enumerate()` 函数会返回一个迭代器，你可以使用 `next()` 函数来逐个获取每个元素及其对应的下标。
例如：
list_example = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(list_example):
    print(index, fruit)

运行这段代码会输出：
0 apple
1 banana
2 cherry

这样，你就可以通过enumerate()函数来同时获取序列中的元素及其下标了。这个函数在需要同时访问元素和下标的情况下非常有用，
比如在某些算法中修改序列元素，同时需要知道其下标时。

除了可迭代对象部分可以扩展知识点， if 表达式 中的 条件表达式 也支持各种布尔运算，如果用中文进行翻译，
表示把满足条件的元素，放置到新的列表中。
"""