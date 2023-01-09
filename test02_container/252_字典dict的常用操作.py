"""
演示字典的常用操作
"""
my_dict = {'mew':120,'dog':89,'pig':10}
# 新增元素
my_dict['rat']=99
print(f"对字典新增后结果：{my_dict}")
# 更新元素
my_dict['pig']=0
print(f"对字典更新后结果：{my_dict}")
# 删除元素 pop()
my_dict = {'mew':120,'dog':89,'pig':10}
score = my_dict.pop('pig')
print(f"删除的元素值是：{score},删除后的结果是：{my_dict}")
# 清空元素 clear()
my_dict = {'mew':120,'dog':89,'pig':10}
my_dict.clear()
print(f"字典被清空，结果是：{my_dict}")
# 获取全部的key keys() --遍历
my_dict = {'mew':120,'dog':89,'pig':10}
keys = my_dict.keys()
print(f"字典的所有key:{keys}")
# 遍历字典 不支持下标索引 使用for循环遍历
# 方式1：通过获取到全部的key来完成遍历
for key in my_dict.keys():
    print(f"字典的key:{key}")
    print(f"字典的值：{my_dict[key]}")
# 方式2：直接对字典进行for循环 直接的到key
for key in my_dict:
    print(f"2字典的key:{key}")
    print(f"2字典的值：{my_dict[key]}")
# 统计字典内的元素数量 len()
num = len(my_dict)
print(f"字典中元素的个数：{num}")
