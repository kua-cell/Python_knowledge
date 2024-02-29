import os
# 获取桌面的路径。

os.path.expanduser("~")   # 获取电脑用户名及路径

# 获取到用户名的路径后，用os.path.join()拼接即可获得桌面路径。

user = os.path.expanduser("~")
desktop = os.path.join(user,'Desktop')
print(user)
print(desktop)
