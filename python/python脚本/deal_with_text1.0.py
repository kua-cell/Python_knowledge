import time

"""
import sys  # 导入sys模块
sys.setrecursionlimit(30000)  # 将默认的递归深度修改为需要的次数
"""

stu_be_input_information: dict = {1001: []
                                  }


def window_content():
    print("*****欢迎使用学生管理系统*****")
    print("1.查询学生信息")
    print("2.添加学生信息")
    print("3.修改学生信息")
    print("4.删除学生信息")
    print("0.退出学生管理")
    return


def main(num: str | int):
    """

    :param num: str | int
    :return:
    """
    num = str(num) or int(num)
    # 类型错误异常处理:
    if type(num) == str | int:
        window_content()
        select_steps(self)
    elif (type(num) != str | int) is TypeError:

        print("输入格式不正确".center(20))
        main(num=input("请重新选择你要办理的项目：\n "
                       "*****欢迎使用学生管理系统***** \n "
                       "1.查询学生信息 \n "
                       "2.添加学生信息 \n "
                       "3.修改学生信息 \n "
                       "4.删除学生信息 \n "
                       "0.退出学生管理 \n "
                       "请选择你要使用的功能, 输入序号 \n "))
    else:
        exit()

    return


def select_steps(self):
    if self.num == 1:
        look_student_information(self)
    elif self.num == 2:
        append_personal_information(self, name=input("姓名:"), sex=input("性别:"), age=input("年龄:"),
                                    school=input("学校地址："), work_address=input("工作地址："), home=input("家庭住址"))
    elif self.num == 3:
        change_stu_information(self)
    elif self.num == 4:
        delete_stu_information(self)
    elif self.num == 0:
        print("程序退出中...")
        exit()
    else:
        print("输入错误，请重新输入")
        main(num)
        return
    return


# 完成一个程序后，进行下一步选择
def select_next_step(self):
    print("1.查询学生信息")
    print("2.添加学生信息")
    print("3.修改学生信息")
    print("4.删除学生信息")
    print("0.退出学生管理")

    self.num = int(input("请选择你要使用的功能"))

    if self.num == 1:
        look_student_information(self)
    elif self.num == 2:
        append_personal_information(self, name=input("姓名:"), sex=input("性别:"), age=input("年龄:"),
                                    school=input("学校地址："), work_address=input("工作地址："), home=input("家庭住址"))
    elif self.num == 3:
        change_stu_information(self)
    elif self.num == 4:
        delete_stu_information(self)
    elif self.num == 0:
        print("程序退出中...")
        exit()
    else:
        print("输入错误，请重新输入")
        return
    return


# 添加个人信息;
def append_personal_information(self, name, sex, age, school, work_address, home):
    self.name = str(name)
    self.sex = str(sex)
    self.age = int(age)
    self.school = str(school)
    self.work_address = str(work_address)
    self.home = str(home)

    if type == str | int:
        try:
            test_type_list = ["name", "sex", "age", "school", "work_address", "home"]
            for i in test_type_list:
                print(type(i))

        except TypeError:
            print("输入格式不对，请重新输入")
            print("_" * 12)
        append_personal_information(self, name=input("姓名:"), sex=input("性别:"), age=input("年龄:"),
                                    school=input("学校地址："), work_address=input("工作地址："), home=input("家庭住址"))
        return
    return


# def re_look_student_information(self):
def look_student_information(self):
    # self.replace()
    self.stu = str(input("请输入被查询人的学号:"))
    # 列表查询，实现个人信息查询：
    if self.stu == stu_be_input_information[self.stu][0]:
        print(f"姓名：{stu_be_input_information[self.stu][0]},\n "
              f"年龄：{stu_be_input_information[self.stu][2]}, \n"
              f"性别：{stu_be_input_information[self.stu][1]}, \n"
              f"家庭地址：{stu_be_input_information[self.stu][5]}, \n")
        if stu_be_input_information[self.stu][5] == "" or "wu" or "无":
            pass
        else:
            print(stu_be_input_information[self.stu][5])
        if stu_be_input_information[self.stu][5] == "" or "wu" or "无":
            pass
        else:
            print(stu_be_input_information[self.stu][5])
        if stu_be_input_information[self.stu][5] == "" or "wu" or "无":
            pass
        else:
            print(stu_be_input_information[self.stu][5])
    select_next_step(self)
    look_student_information(self)
    return


def change_stu_information(self):
    self.changed_stu_information = str(input("想要修改个人信息的学号："))
    if self.changed_stu_information == stu_be_input_information[self.changed_stu_information]:
        print("请输入你要修改的选项")
        new_stu_information = str(input("-----------------"
                                        "选项：1.姓名 \n"
                                        "     2.性别 \n"
                                        "     3.年龄 \n"
                                        "     4.学校 \n"
                                        "     5.家庭地址 \n"
                                        "     6.工作地址 \n"))
        if new_stu_information == 1:
            list.insert(self=stu_be_input_information[self.changed_stu_information][0], __index=0,
                        __object=input("需要修改的家庭地址："))
            print("修改成功")
            input("请选择下一步:")
            select_next_step(self)
        if new_stu_information == 2:
            list.insert(self=stu_be_input_information[self.changed_stu_information][1], __index=1,
                        __object=input("需要修改的家庭地址："))
            print("修改成功")
            input("请选择下一步:")
            select_next_step(self)
        if new_stu_information == 3:
            list.insert(self=stu_be_input_information[self.changed_stu_information][2], __index=2,
                        __object=input("需要修改的家庭地址："))
            print("修改成功")
            input("请选择下一步:")
            select_next_step(self)
        if new_stu_information == 4:
            list.insert(self=stu_be_input_information[self.changed_stu_information][3], __index=3,
                        __object=input("需要修改的家庭地址："))
            print("修改成功")
            input("请选择下一步:")
            select_next_step(self)
        if new_stu_information == 5:
            list.insert(self=stu_be_input_information[self.changed_stu_information][4], __index=4,
                        __object=input("需要修改的家庭地址："))
            print("修改成功")
            input("请选择下一步:")
            select_next_step(self)
        if new_stu_information == 6:
            list.insert(self=stu_be_input_information[self.changed_stu_information][5], __index=5,
                        __object=input("需要修改的家庭地址："))
            print("修改成功")
            input("请选择下一步:")
            select_next_step(self)
            return
        return
    else:
        another_chance = input("您要查询的姓名不存在，是否需要添加个人信息")
        if another_chance == ["是", "shi", "y", "ye", "yes", "Y"]:
            append_personal_information(self, name=input("姓名:"), sex=input("性别:"), age=input("年龄:"),
                                        school=input("学校地址："), work_address=input("工作地址："),
                                        home=input("家庭住址"))
        elif another_chance == ["否", "fou", "n", "no"]:
            print("即将退出")
            print(time.sleep(3))
            exit()
        else:
            pass

    return


def delete_stu_information(self):
    """
    @param: new_dict: dict
    """
    self.deleted_stu_information = input("您要删除部分信息的学号:")
    if self.deleted_stu_information == stu_be_input_information[self.deleted_stu_information]:
        dict.pop(self=stu_be_input_information, __key=[self.deleted_stu_information], __default="不存在该信息")
        print(stu_be_input_information)
        select_next_step(self)
    else:
        print("还有3秒后，即将退出！")
        time.sleep(3)
        exit()
    return


main(num)
