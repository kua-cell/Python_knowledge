# if else 语句练习
from random import random

age = int(18)
if int(input("请输入你的年龄：")) < int(18):
    print("你可免票，祝你游玩愉快。")
else:
    print("你已成年，还需补票10元.")
print("祝你路途愉快")
# 判断语句的综合练习:

num = random.randint(1, 10)

guess_num = int(input("请输入你要猜的数字："))

if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")
