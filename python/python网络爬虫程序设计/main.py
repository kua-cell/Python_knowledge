# 首先获取想要爬取网站内容的url链接
import time

import requests
from bs4 import BeautifulSoup


url = "https://www.crazyant.net"

# 通过赋值给变量r，利用requests库中的requests.get()方法向网站发起访问请求
r = requests.get(url)
"""判断状态码是否为200，检测请求访问是否成功否则就退出程序"""
if r.status_code != 200:
    raise Exception()

"""将r.text（获取到完整的html源代码，除了css和js文件内容）赋值给html_doc变量"""
html_doc = r.text

"""
该方法中的self和features参数分别赋值为html_doc和html.parser
通过导入的BeautifulSoup方法赋值给soup变量，将网页中的源代码给获取到
"""

soup = BeautifulSoup(html_doc, "html.parser")
"""
部分网页会出现类似新闻网站中，一个容器里装有多条新闻，每个新闻都有属于自己的超链接、
即会发生跳转，这红也米娜的源代码中可能会是嵌套在相同的元素中，但是这个元素有很多个，
通过soup.find_all()方法:
find_all(name:, attrs:,recursive:,string:,limit:, **kwarg:)
如果元素属性中标有class类名等标志性属性，可通过该属性准确的查找html中符合的所有元素
"""
h2_nodes = soup.find_all("h2", class_="entry-title")

"""
通过for循环，将h2_nodes中的得到的h2元素所在区域的代码循环遍历
同时通过.find("元素名")依次找出
"""
for h2_node in h2_nodes:
    # 通过下行代码，将变量link变成一个列表的形式
    link = h2_node.find("a")

    print(link["href"], link.get_text())
    """增加睡眠时间，减少访问频率"""
    time.sleep(3)
