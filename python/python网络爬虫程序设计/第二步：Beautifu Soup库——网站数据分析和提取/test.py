from bs4 import BeautifulSoup


"""
获取源代码后进行网页分析,
将源代码保存于html文件中,
再用with as 语句打开html文件.
"""
with open("firefoxchina.html", encoding="UTF-8") as fin:
    """firefoxchina.html来自火狐主页url2 = 'https://home.firefoxchina.cn/'"""
    html_doc = fin.read()

# 调用BeautifulSoup， 指定传入参数
soup: BeautifulSoup = BeautifulSoup(html_doc, "html.parser")
# 通过find_all方法查询大块区域的代码信息：
links = soup.find_all(name=input("HTML源代码中元素名称："))
for link in links:
    """
    link.name用来查找每个元素名称；
    link[]中的元素为html中元素的属性
    link.get_text()可以将某个区域元素的域名， 或者元素内的标记的文本名称
    """
    print(link.name, link["href"], link.get_text(), end="")

# 使用find方法找寻特定区域html源代码：
div_node = soup.find("div", id="content")
print(div_node)

# 使用find方法找寻特定区域html源代码：
img = soup.find(name="img")
print(img['src'])
