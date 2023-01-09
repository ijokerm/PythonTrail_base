"""
演示全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取数据文件
f = open("E:\BaiduNetdiskDownload\Python课件\资料\可视化案例数据\地图数据\疫情.txt",'r',encoding='UTF-8')
data = f.read()
f.close()
# 取全国各地的数据
# 将json字符串转化为python字典
data_dict = json.loads(data)
# 从字典中取出省份数据
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组 并将各个省的数据都封装到列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"] # 省份名称
    province_confirm = province_data["total"]["confirm"] # 确诊人数
    data_list.append((province_name,province_confirm))
print(data_list)
# 添加地图
map = Map()
map.add("各省份确诊人数",data_list,"china")
# 设置全局变量，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#EEEED1"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFC1C1"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF6A6A"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FFD700"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#FF6347"},
            {"min": 100000,  "label": "100000+", "color": "#DC143C"}
        ]
    )
)
map.render()