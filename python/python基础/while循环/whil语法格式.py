# 循环语句（1）{while+条件:}:
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1

print("1累加100次后的结果为：%s" % sum)
# 获取1——100的随机数字
import random

num = random.randint(1, 100)
# 定义一个变量，记录总共猜了了多少次
count = 0
# 通过一个布尔类型的变量，做循环是否继续的标记
falg = True
while falg:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        # 设置为false就是终止循环的条件
        falg = False
    else:
        if guess_num > num:
            print("你猜得大了")
        else:
            print("你猜的小了")

print(f"你总共猜了{count}次")
