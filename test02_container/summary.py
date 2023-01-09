"""
演示数据容器的通用功能
"""
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {'k1':1,'k2':2,'k3':3,'k4':4,'k5':5}
# len 元素个数
print(f"列表 元素个数：{len(my_list)}")
print(f"元组 元素个数：{len(my_tuple)}")
print(f"字符串 元素个数：{len(my_str)}")
print(f"集合 元素个数：{len(my_set)}")
print(f"字典 元素个数：{len(my_dict)}")
# max(容器) 最大元素
print(f"列表 最大的元素： {max(my_list)}")
print(f"元组 最大的元素： {max(my_tuple)}")
print(f"字符串最大的元素：：{max(my_str)}")
print(f"集合 最大的元素： {max(my_set)}")
print(f"字典 最大的元素： {max(my_dict)}")
# min 最小元素
print(f"列表 最小的元素： {min(my_list)}")
print(f"元组 最小的元素： {min(my_tuple)}")
print(f"字符串最小的元素：：{min(my_str)}")
print(f"集合 最小的元素： {min(my_set)}")
print(f"字典 最小的元素： {min(my_dict)}")
# 类型转换 容器转列表 list()
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是：{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是：{list(my_dict)}")
# 类型转换 容器转元组 tuple()
print(f"列表转元组的结果是： {tuple(my_list)}")
print(f"元组转元组的结果是： {tuple(my_tuple)}")
print(f"字符串转元组的结果是：{tuple(my_str)}")
print(f"集合转元组的结果是： {tuple(my_set)}")
print(f"字典转元组的结果是： {tuple(my_dict)}")
# 类型转换 容器转字符串
print(f"列表转字符串的结果是： {str(my_list)}")
print(f"元组转字符串的结果是： {str(my_tuple)}")
print(f"字符串转字符串的结果是：{str(my_str)}")
print(f"集合转字符串的结果是： {str(my_set)}")
print(f"字典转字符串的结果是： {str(my_dict)}")
# 类型转换 容器转集合
print(f"列表转集合的结果是： {set(my_list)}")
print(f"元组转集合的结果是： {set(my_tuple)}")
print(f"字符串集合的结果是：{set(my_str)}")
print(f"集合转集合的结果是： {set(my_set)}")
print(f"字典转集合的结果是： {set(my_dict)}")
# sorted() 排序
my_list = [3,1,4,2,5]
my_tuple = (4,1,5,2,3)
my_str = "abecdfg"
my_set = {3,5,4,1,2}
my_dict = {'k2':2,'k3':3,'k1':1,'k4':4,'k5':5}
print(f"列表对象的排序结果是： {sorted(my_list)}")
print(f"元组对象的排序结果是： {sorted(my_tuple)}")
print(f"字符串对象的排序结果是： {sorted(my_str)}")
print(f"集合对象的排序结果是： {sorted(my_set)}")
print(f"字典对象的排序结果是： {sorted(my_dict)}") # 字典排序丢失value
# 反向排序
print(f"列表对象的反向排序结果是： {sorted(my_list,reverse=True)}")
print(f"元组对象的反向排序结果是： {sorted(my_tuple,reverse=True)}")
print(f"字符串对象的反向排序结果是： {sorted(my_str,reverse=True)}")
print(f"集合对象的反向排序结果是： {sorted(my_set,reverse=True)}")
print(f"字典对象的反向排序结果是： {sorted(my_dict,reverse=True)}")