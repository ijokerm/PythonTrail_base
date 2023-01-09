"""
演示pyecharts入门
"""
# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 创建一个折线图对象
line = Line()
# 给折线图对象添加X轴数据
line.add_xaxis(["中国","美国","英国"])
# 给折线图对象添加Y轴数据
line.add_yaxis("GDP",[30,20,10])
# 设置全局变量 set_global_opts pos-position
line.set_global_opts(
    title_opts=TitleOpts("国际GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)

)
# 通过render方法，将代码生成为图像
line.render()
