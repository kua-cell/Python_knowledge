"""
演示基础柱状图的开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts

# 使用Bar构建基 础柱状图
bar1 = Bar()
# 分别添加X,Y轴的数据
bar1.add_xaxis(["中国", "美国", "英国", "法国", "日本"])
bar1.add_yaxis("GDP", [30, 20, 10, 12, 15], label_opts=LabelOpts(position="right"))
# 反转X，Y轴的数据
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国", "法国", "日本"])
bar2.add_yaxis("GDP", [50, 30, 30, 20, 23], label_opts=LabelOpts(position="right"))
# 反转X，Y轴的数据
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国", "法国", "日本"])
bar3.add_yaxis("GDP", [78, 45, 50, 34, 41], label_opts=LabelOpts(position="right"))
# 反转X，Y轴的数据
bar3.reversal_axis()
# 创建时间线对象;在timeline()中输入一个字典'{}'
timeline = Timeline({"theme": ThemeType.LIGHT})
# timeline对象添加bar柱状图
timeline.add(bar1, "2020年GDP")
timeline.add(bar2, "2022年GDP")
timeline.add(bar3, "2023年GDP")
# 设置一个自动播放
timeline.add_schema(
    play_interval=1000,                 # 自动播放的时间间隔（毫秒）
    is_timeline_show=True,              # 是否自动播放的时候，显示时间线
    is_auto_play=True,                  # 是否自动播放
    is_loop_play=True                   # 是否循环自动播放
)

# 通过时间线绘图(绘图用时间线绘图，而不是bar对象了，该换成timeline)
timeline.render("基础柱状图—时间线.html")