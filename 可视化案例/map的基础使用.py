"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()
# 准备数据
data = [
    ("北京",99),
    ("上海",199),
    ("湖南",299),
    ("台湾",399),
    ("广东",499)
]
# 添加数据
map.add("测试地图",data,"china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#EEEED1"},
            {"min":10,"max":99,"label":"10-99","color":"#FFC1C1"},
            {"min":100,"max":999,"label":"100-999","color":"#FF6A6A"},
            {"min":1000,"max":9999,"label":"1000-9999","color":"#FF0000"},
        ]
    )
)
# 绘图
map.render()