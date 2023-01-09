"""
演示json数据和Python字典的相互转换
"""
import json
# 准备列表，内嵌元素为字典，将其转换为json
data = [{"name":'朱翠花1号',"age":21}, {"name":'朱翠花2号',"age":22}, {"name":'朱翠花3号',"age":23}]
json_str = json.dumps(data,ensure_ascii=False)
print(json_str,type(json_str))
# 准备字典，将字典转换为json
d = {"name":'朱翠花大坏蛋',"gender":'男'}
json_d = json.dumps(d,ensure_ascii=False)
print(json_d,type(json_d))
# 将json字符串转换为Python数据类型[{k:v,k:v},{k:v,k:v}]
s = '[{"name":"朱翠花1号","age":21}, {"name":"朱翠花2号","age":22}, {"name":"朱翠花3号","age":23}]'
list_j = json.loads(s)
print(type(list_j))
print(list_j)
# 将json字符串转换为Python数据类型{k:v,k:v}
str = '{"name":"朱翠花大坏蛋","gender":"男"}'
dj = json.loads(str)
print(type(dj))
print(dj)