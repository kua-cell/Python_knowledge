def list_for_func():
    my_list: list[int] = [1, 2, 3, 4]
    # for 临时变量 in 数据容器

    for element in my_list:
        print(f"列表中的元素：{element}")


list_for_func()

# 定义字典
my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1}, 类型：{type(my_dict1)}")
print(f"字典1的内容是：{my_dict2}, 类型：{type(my_dict2)}")
print(f"字典1的内容是：{my_dict3}, 类型：{type(my_dict3)}")

# 定义重复Key的字典
# my_dict1 = {"王力宏": 99, "王力宏": 88, "林俊杰": 77}
# print(f"重复Key字典1的内容是：{my_dict1}")
# 从字典中基于Key获取Value
# my_dict1 = {"王力宏": 99, "周杰伦": 88, "林俊杰": 77}
# score = my_dict1["王力宏"]
# print(f"王力宏的分数是：{score}")
# 定义一个嵌套字典
stu_score_dict = {
    "王力宏": {"语文": 83, "数学": 94, "英语": 86},
    "周杰伦": {"语文": 92, "数学": 87, "英语": 95},
    "林俊杰": {"语文": 78, "数学": 64, "英语": 74}
}
print(f"学生的考试信息是: {stu_score_dict}")
# 获取嵌套字典的信息
score = stu_score_dict['周杰伦']['语文']
print(f"周杰伦的语文分数：{score}")

print(list_for_func)
