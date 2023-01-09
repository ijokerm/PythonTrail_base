# 定义一个列表记录学生的年龄
# 1、定义变量接收列表
age_list = [21,25,21,23,22,20]
print(f"1、定义列表初始值：{age_list}")
# 2、追加一个数字3到列表尾部 append
age_list.append(31)
print(f"2、追加一个元素在尾部后，列表为：{age_list}")
# 3、追加一个新列表[29,33,30] extend
list_1 = [29,33,30]
age_list.extend(list_1)
print(f"3、追加一个新列表[29,33,30],列表为：{age_list}")
# 4、取出第一个元素--21 从前往后第一个- 0
element = age_list[0]
print(f"4、取出第一个元素后，列表为：{element}")
# 5、取出最后一个元素 30 从后往前第一个 -1
element2 = age_list[-1]
print(f"5、取出最后一个元素后，列表为：{element2}")
# 6、查找元素31，在列表中的下标位置 index
index = age_list.index(31)
print(f"6、元素31，在列表中的下标位置：{index}")