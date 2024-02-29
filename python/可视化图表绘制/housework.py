# 导包
from pyecharts.charts import Line

# 创建一个折线图对象
line = Line()
# 给折线图对象添加X轴的数据
line.add_xaxis(["中国", "美国", "英国"])
# 给折线图对象添加Y轴的数据
line.add_yaxis("GDP", [30, 20, 10])
# 通过render方法，将代码生成为图像
line.render()
