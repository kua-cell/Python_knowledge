import os
# ��ȡ�����·����

os.path.expanduser("~")   # ��ȡ�����û�����·��

# ��ȡ���û�����·������os.path.join()ƴ�Ӽ��ɻ������·����

user = os.path.expanduser("~")
desktop = os.path.join(user,'Desktop')
print(user)
print(desktop)
