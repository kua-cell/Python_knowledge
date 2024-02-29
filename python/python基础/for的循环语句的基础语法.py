# 统计如下字符串中，有几个字母a
name = "it heima is a brand of it cast"
# 定义一个变量，用来统计有多少个a
count = 0
# for循环统计
# for 临时变量 in 被统计的数据：
for i in name:
    if i == "a":
        count += 1

print(f"被统计的字符串中有{count}个a")

# range语句的基本使用
"""range 语法2 range(num1)
for x range(10):
    print(x)

range 语法2 range(num1,num2)
for x range (5,10):
     从5开始，到10结束（不包含10本身）的一个数字序列，数字之间间隔为1（默认）
     print(x)

range 语法3 range (num1,num2,step)
for x in  range(5,10,2):
    从5开始，到10结束（不包含10本身）的一个数字序列，数字之间间隔为2
#print(x)
"""