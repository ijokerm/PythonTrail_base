"""
演示数据容器字典的定义
"""
# 定义字典 key:value  --为一个元素
my_dict1 = {"moew":100,"piggy":0,"doggy":22}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1内容：{my_dict1},类型{type(my_dict1)}")
print(f"字典2内容：{my_dict2},类型{type(my_dict2)}")
print(f"字典3内容：{my_dict3},类型{type(my_dict3)}")
# 定义重复key的字典 key不允许重复
my_dict4 = {"piggy":100,"piggy":0,"doggy":22}
print(f"重复key的字典内容是：{my_dict4}")
# 从字典中基于key获取value
my_dict1 = {"moew":100,"piggy":0,"doggy":22}
score = my_dict1["moew"]
print(f"moew中对应的值是：{score}")
score = my_dict1["piggy"]
print(f"piggy中对应的值是：{score}")
# 定义嵌套字典
info_dict = {
    "moew":{
        '语文':88,
        '数学':90,
        '英语':100
    },"piggy":{
        '语文':78,
        '数学':80,
        '英语':90
    },"doggy":{
        '语文':68,
        '数学':70,
        '英语':60
    }
}
print(info_dict)
# 从嵌套字典中获取数据 看一下 doggy 数学
score = info_dict["doggy"]['数学']
print(f"doggy的数学：{score}")