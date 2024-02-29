· 创建BeautifulSoup对象
from bs4 import BeautifulSoup
# 根据HTML网页字符串创建BeautifulSoup对象
>>> soup = BeautifulSoup(
>                   html_doc,                   # HTML文档字符串
>                   'html.parser'，             # HTML解析器
>                   from_encoding='utf-8'      #  HTML文档的编码   
)


[/搜索节点/]: # (find_all， find)
# 方法： find_all(name, attrs, string)
# 查找所有标签为a的节点：
soup.find_all('a')

# 查找所有标签为a， 链接符合....形式的节点
soup.find_all('a', href="....")

# 查找所有标签为div， class为'...', 文字为Python的节点
soup.find_all('div', class= "...", string="Python")

[/访问节点信息/]: # (node)
# 得到节点为：
例如： <a href="....">Python</a>
# 获取查找到的节点标签名称
node.name
# 获取查找到的a节点的href属性：
node['href']
# 获取查找到的a节点的链接文字：
node.get_text()

