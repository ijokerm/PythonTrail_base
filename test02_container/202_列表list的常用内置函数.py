"""
演示list的常用操作
"""
my_list = ['quen','king','diff','python']
# 1.1查找某元素在列表中的下标索引
index = my_list.index('diff')
print(f"diff在列表中的下表索引值：{index}")
# 1.2如果查找某元素在列表中的下标索引不存在，报错:ValueError: 'jiff' is not in list
# index = my_list.index('jiff')
# print(f"diff在列表中的下表索引值：{index}")

# 2.修改特定下标索引的值
my_list[1] = 'lydia'
print(f"列表修改元素值后，结果是{my_list}")
# 3.在指定下标位置插入新元素 语法：列表.insert(下标，元素)
my_list.insert(2,'sunrise')
print(f"列表修改元素值后，结果是{my_list}")
# 4.在列表的尾部追加‘’‘单个’‘’新元素 语法：列表.append(元素)
my_list.append('tail')
print(f"列表在尾部追加一个元素值后，结果是{my_list}")
# 5.在列表的尾部追加‘’‘一批’‘’新元素
my_list1 = ['1,2',True]
my_list.extend(my_list1)
print(f"列表追加一个新的列表（数据容器）值后，结果是{my_list}")
# 6.删除指定下标索引的元素 2种方式
my_list = ['quen', 'lydia', 'diff', 'python']
# 6.1方式1：del
del my_list[2] # 删除'diff'
print(f"列表删除元素后结果是：{my_list}")
# 6.2方式2：列表.pop(下标) pop()本质是将指定下标的元素取出来然后返回出去 --即就是能得到返回值，同时也将元素从列表中移除掉了
my_list = ['quen', 'lydia', 'diff', 'python']
element = my_list.pop(2)
print(f"通过pop方法取出的元素为{element},取出元素后列表为：{my_list}")
# 7.删除某元素在列表中的第一个匹配项 语法 列表.remove(元素)
my_list = ['quen', 'lydia', 'diff', 'python','diff','lydia']
my_list.remove('diff')
print(f"通过remove方法移除值为‘diff’的元素后，列表的结果是：{my_list}")
# 8.清空列表  列表.clear()
my_list.clear()
print(f"列表被清空，结果是：{my_list}")
# 9.统计列表内某元素的数量 语法：列表.count(元素)
my_list = ['quen', 'lydia', 'diff', 'python','diff','lydia']
count = my_list.count('lydia')
print(f"列表中‘lydia'的数量为：{count}")
# 10.统计列表内全部元素的数量  len(列表)
my_list = ['quen', 'lydia', 'diff', 'python','diff','lydia']
count = len(my_list)
print(f"列表中元素的数量为：{count}")


