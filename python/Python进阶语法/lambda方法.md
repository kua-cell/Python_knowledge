Python lambda 表达式是什么
lambda 表达式也叫做匿名函数，在定义它的时候，没有具体的名称，一般用来快速定义单行函数，直接看一下基本的使用：

fun = lambda x:x+1
print(fun(1))
查看上面的代码就会发现，使用 lambda 表达式定义了一行函数，没有函数名，后面是是函数的功能，对 x 进行 +1 操作。
稍微整理一下语法格式：

lambda [参数列表]:表达式
# 英文语法格式
lambda [arg1[,arg2,arg3....argN]]:expression
语法格式中有一些注意事项：

lambda 表达式必须使用 lambda 关键字定义；
lambda 关键字后面，冒号前面是参数列表，参数数量可以从 0 到任意个数。多个参数用逗号分隔，冒号右边是 lambda 表达式的返回值。
本文开始的代码，如果你希望进行改写成一般函数形式，对应如下：

fun = lambda x:x+1
# 改写为函数形式如下：
def fun(x):return x+1
当然，如果你决定上述 fun() 也多余，匿名函数就不该出现这些多余的内容，你也可以写成下面这个样子，
不过代码的可读性就变低了。

print((lambda x:x+1)(1))
lambda 表达式一般用于无需多次使用的函数，并且该函数使用完毕就释放了所占用的空间。

怎么用
lambda 表达式与 def 定义函数的区别
第一点：一个有函数名，一个没有函数名

第二点：lambda 表达式 : 后面

只能有一个表达式，多个会出现错误，也就是下面的代码是不会出现的。

# 都是错误的
lambda x:x+1 x+2
由于这个原因的存在，很多人也会把 lambda 表达式称为单表达式函数。

第三点：for 语句不能用在 lambda 中

有的地方写成了 if 语句和 print 语句不能应用在 lambda 表达式中，该描述不准确，例如 下述代码就是正确的。

lambda a: 1 if a > 10 else 0
基本结论就是：lambda 表达式只允许包含一个表达式，不能包含复杂语句，该表达式的运算结果就是函数的返回值。

第四点：lambda 表达式不能共享给别的程序调用

第五点：lambda 表达式能作为其它数据类型的值
例如下述代码，用 lambda 表达式是没有问题的。

my_list = [lambda a: a**2, lambda b: b**2]
fun = my_list[0]
print(fun(2))
lambda 表达式应用场景
在具体的编码场景中，lambda 表达式常见的应用如下：

1. 将 lambda 表达式赋值给一个变量，然后调用这个变量
上文涉及的写法多是该用法。

fun = lambda a: a**2
print(fun(2))
2. 将 lambda 表达赋值给其它函数，从而替换其它函数功能
一般这种情况是为了屏蔽某些功能，例如，可以屏蔽内置 sorted 函数。

sorted = lambda *args:None
x = sorted([3,2,1])
print(x)
3. 将 lambda 表达式作为参数传递给其它函数
在某些函数中，函数设置中是可以接受匿名函数的，例如下述排序代码：

my_list = [(1, 2), (3, 1), (4, 0), (11, 4)]
my_list.sort(key=lambda x: x[1])
print(my_list)
my_list 变量调用 sort 函数，参数 key 赋值了一个 lambda 表达式，
该式子表示依据列表中每个元素的第二项进行排序。

4. 将 lambda 表达式应用在 filter、map、reduce 高阶函数中
这个地方先挖下一个小坑，你可以自行扩展学习。

5. 将 lambda 表达式应用在函数的返回值里面
这种技巧导致的结论就是函数的返回值也是一个函数，具体测试代码如下：

def fun(n):
    return lambda x:x+n

new_fun = fun(2)
print(new_fun)
# 输出内容：<function fun.<locals>.<lambda> at 0x00000000028A42F0>
上述代码中，lambda 表达式实际是定义在某个函数内部的函数，称之为嵌套函数，或者内部函数。
对应的将包含嵌套函数的函数称之为外部函数。
内部函数能够访问外部函数的局部变量，这个特性是闭包(Closure)编程的基础，
滚雪球学 Python 第二轮也会有专门的一篇博客去介绍闭包编程相关知识。

扩展知识
lambda 表达式虽然有优点，但不应过度使用 lambda，最新的官方 Python 风格指南 PEP8 建议永远不要编写下述代码：

normalize_case = lambda s: s.casefold()
因此你想创建一个函数并存储到变量中, 请使用 def 来定义。

不必要的封装
我们实现一个列表排序，按照绝对值大小进行。

my_list = [-1,2,0,-3,1,1,2,5]
sorted_list = sorted(my_list, key=lambda n: abs(n))
print(sorted_list)
上述貌似用到了 lambda 表达式，但是确忘记了，在 Python 中所有的函数都可以当做参数传递。

my_list = [-1,2,0,-3,1,1,2,5]
sorted_list = sorted(my_list, key=abs)
print(sorted_list)
也就是当我们有一个满足要求的函数的时候，没有必要在额外的去使用 lambda 表达式了。