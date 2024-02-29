import math

a = -2
abs(a)  # absolute 绝对值
round(a)  # 四舍五入
pow(a, 2)  # 取幂

print(math.ceil(a))
print(math.floor(a))

# 字符串方法

strings1 = "wueiw nwe"

print(len(strings1))
print(strings1.capitalize)  # 将第一个字母大写

print(strings1.upper())  # 将所有字母改为大写

print(strings1.lower())  # 将所有字母改为小写

print(strings1.replace("wue", "world"))  # 将自负床中某一段字符串更改

print(strings1.find("world"))  # 如果没加双引号，将会识别为变量名

# boolean  布尔类型

a = True

B = False

print(strings1.isupper())  # 识别字符串是否全部都是大写
