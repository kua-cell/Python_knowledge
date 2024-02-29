"""
递归——在编程中是一种非常重要的算法
递归： 即方法（函数）自己调用自己的一种特殊编程方法
如:
def func():

    if ...:
        func()

    return ...

像这样那个在内部函数调用外部函数的方法， 称之为递归调用
"""
import os


def test_os():
    """演示os模块的3个基础方法"""
    print(os.listdir("D:\电脑管家迁移文件"))  # 可列出所提供的文件夹目录下的内容
    print(os.path.isdir("D:\电脑管家迁移文件\微信聊天记录搬家"))  # 判断指定路径是否为文件夹
    print(os.path.exists("D:\电脑管家迁移文件"))  # 判断路径是否存在


def get_files_recursion_from_dir(path):
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    Parameters
    ----------
    path: 被判断的文件夹

    :Returns: list. 包含全部的文件，如果目录不存在或者无文件就返回一个空的list
    -------

    """
    print(f"当前判断的是{path}")
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):     # 如果不是文件夹，则程序终止
                # 进入到这里，表明这个目录是文件夹不是文件
                file_list += get_files_recursion_from_dir(new_path)
                #  “file_list +=”将所有判断出来的文件返回到一个list中呈现出来
            else:
                file_list.append(new_path)
# 注意返回值的传递，确保从最内层，层层传递到最外层
    else:
        print(f"指定目录{path}不存在")
        return []

    return file_list


if __name__ == '__main__':
    print(get_files_recursion_from_dir("D:\电脑管家迁移文件"))

#        第一次：
#        微信聊天记录搬家
#        第二次（递归）D:\电脑管家迁移文件\微信聊天记录搬家：
#        WeChat Files
#        第三次（递归）D:\电脑管家迁移文件\微信聊天记录搬家\WeChat Files：
#        以下全是文件夹
#        All Users
#        Applet
#        WMPF
#        wxid_3ubwljezfs9k22
#        wxid_7r4xh71bkx8u22
#        wxid_d5wew151wr1922
#        wxid_muhj2vf9w2kt22
#        wxid_pne9j06rc05a22
#        wxid_yh9r0jfa473522
#        第四次（递归）D:\电脑管家迁移文件\微信聊天记录搬家\WeChat Files\All Users：
#        文件夹：
#        config
#        文件(或图片)：
#        02fbbcc44176e4941042e33014ca4586
#        4aebdbb57cf84d99c7b759ea957a0ed4
#        3bdf460935be661d14f785795f304f40
#        ......
#
#        ......