import re

s = '1python itheima itcast python jiang'
# match 从头匹配      开头不匹配，结果为：None
result = re.match('python', s)
print(result)
# search 搜索整个字符串，找出匹配。从前到后，找到第一个就停止，不再继续往后
# 若找不到 返回一个  None
result1 = re.search('python', s)
print(result1)
# findall 匹配整个字符串，找出所有匹配项

result2 = re.findall('python', s)
print(result2)
# 若没有，返回空list:[]
# 即：[]
