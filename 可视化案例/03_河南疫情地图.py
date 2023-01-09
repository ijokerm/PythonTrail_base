"""
演示河南省的疫情地图
"""
import json
from pyecharts.charts import *
from pyecharts.options import *
# 读取数据文件
f = open("E:\BaiduNetdiskDownload\Python课件\资料\可视化案例数据\地图数据\疫情.txt",'r',encoding='UTF-8')
data =f.read()
# 关闭文件
f.close()
# 将json数据---python字典
data_dict = json.loads(data)
# 取河南省的数据
data_list = data_dict["areaTree"][0]["children"][3]["children"]
# 取河南省各个市的数据
res_list = []
for data in data_list:
    name = data["name"]+"市"
    num = data["total"]["confirm"]
    res_list.append((name,num))
print(res_list)
# 单独添加济源市数据
res_list.append(('济源市',5))
# 添加地图
map = Map()
# 在地图中添加数据
map.add("河南确诊人数",res_list,"河南")
# 设置地图全局配置
map.set_global_opts(
    title_opts=TitleOpts(title="河南疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=(
            {"min":1,"max":9,"label":"1-9","color":"#EEEED1"},
            {"min":10,"max":99,"label":"10-99","color":"#FFC1C1"},
            {"min":100,"max":999,"label":"100-999","color":"#FF6A6A"},
            {"min":1000,"max":9999,"label":"1000-9999","color":"#FF0000"}
        )
    )
)
map.render()


