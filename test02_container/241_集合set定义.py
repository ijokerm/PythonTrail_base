"""
演示数据容器集合的使用
"""
# 定义集合 不重复、无序
my_set = {"春天的熊","joker","blame",True,21,'blame'}
my_set_empty = set()   # 定义空集合
print(f"my_set的内容：{my_set},类型是：{type(my_set)}")
print(f"my_set_empty的内容：{my_set_empty},类型是：{type(my_set_empty)}")
# 添加新元素 add()
my_set.add('jizz')
my_set.add('joker') # 重复的不会添加
print(f"添加元素后结果：{my_set}")
# 移除元素 remove()
my_set.remove(True)
print(f"移除元素后结果：{my_set}")
# 随机取出一个元素 pop()
my_set = {"春天的熊","joker","blame",21}
element = my_set.pop()
print(f"随机取出的元素是：{element},取出后集合结果为{my_set}")
# 情空集合 clear()
my_set.clear()
print(f"集合被清空了，结果是{my_set}")
# 取两个集合的差集 集合1.difference(集合2) --取出集合1有而集合2没有的元素
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"set1={set1},set2={set2},取出差集后的结果：{set3}")
# 消除2个集合差集 difference_update()
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"消除差集后：set1={set1},set2={set2}")
# 2个集合合并为一个 union()
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"set1={set1},set2={set2},合并后集后的结果：{set3}")
# 统计集合元素数量 len()
set1 = {1,2,3,'fu*k'}
num = len(set1)
print(f"{set1}中元素数量为：{num}")

#集合的遍历 集合不支持下标索引，不能用while循环。可以用for循环
set1 = {1,2,3,'fu*k'}
for element in set1:
    print(f"{set1}中的元素：{element}")

