1. 导入 requests模块：
>>> import requests

2. 调用 get 方法：
>>> r = requests.get('https://www.douban.com/')

3. 将获得的 html 文件写入本地：
>>>with open('test.html','w',encoding='utf-8') as f:
        f.write(r.text)


· “test.html” 是文件名，一般情况下建议填写绝对路径。如果直接这样写，文件保存在当前目录。
· encoding是必须的，因为在windows下面，新文件的默认编码是gbk，这样的话，python解释器会用gbk编码去解析我们的网络数据流txt，然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了

[/代码总结/]: 

>>> import requests
>>> r = requests.get('https://www.douban.com/') # 豆瓣首页
>>> with open('test.html','w',encoding='utf-8') as f:
    f.write(r.text)

原文链接：https://blog.csdn.net/qq_38866586/article/details/100129427