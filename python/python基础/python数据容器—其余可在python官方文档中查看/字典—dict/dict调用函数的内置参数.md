# dict.pop()���������ò�����

Python �ֵ� pop() ����ɾ���ֵ������ key ����Ӧ��ֵ������ֵΪ��ɾ����ֵ��key ֵ��������� ���򣬷��� default ֵ��

�﷨
pop()�����﷨��

pop(key[,default])
����
key: Ҫɾ���ļ�ֵ
default: ���û�� key������ default ֵ
����ֵ
���ر�ɾ����ֵ��

ʵ��
����ʵ��չʾ�� pop() ������ʹ�÷�����

ʵ��
#!/usr/bin/python
# -*- coding: UTF-8 -*-

site= {'name': '����̳�', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print pop_obj    # ��� ������̳�
