"""
演示第三个图表，GDP动态柱状图开发
"""
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import *
# 读取数据
f = open("E:/1960-2019全球GDP数据.csv",'r',encoding='GB2312')
data_lines = f.readlines()
# 关闭文件
f.close()

# 删除不必要数据 --第一条
data_lines.pop(0)
# 将数据转化为字典格式
#格式为：{ 年份: [ [国家, gdp], [国家,gdp]], ......
data_dict = {}
for line in data_lines:
   year = int(line.split(",")[0])   # 年份
   country = line.split(",")[1]     # 国家
   gdp = float(line.split(",")[2])  # GDP
   # 如何判断字典里面有没有指定的key？ 利用异常捕获
   try:
       data_dict[year].append([country,gdp])
   except KeyError as e:
       data_dict[year] = []
       data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})
# 排序年份
year_list = sorted(data_dict.keys())
for year in year_list:
    # 将年份里面的GDP进行排序
    data_dict[year].sort(key= lambda element:element[1],reverse=True)
    # 切片取前八
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for tmp_cg in year_data:
        x_data.append(tmp_cg[0])
        y_data.append(tmp_cg[1])
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    # 反转x y轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年的全球GDP前八数据")
    )
    # for循环每一年的数据，基于每一年的数据创建bar对象
    # 在for中将每一年的bar对象添加到时间线中
    timeline.add(bar,str(year))

# 设置时间线自动播放点
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_loop_play=True,
    is_auto_play=True
)
# 绘图
timeline.render("1968-2019全球GDP前8国家.html")