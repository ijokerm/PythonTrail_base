"""
演示元组tuple定义和操作
"""
# # 定义元祖
# t1 = (1,'jerk',True)
# t2 = ()
# t3 =tuple()
# print(f"t1的类型是：{type(t1)},内容是：{t1}")
# print(f"t2的类型是：{type(t2)},内容是：{t2}")
# print(f"t3的类型是：{type(t3)},内容是：{t3}")
#
# # 定义单个元素的元素 后面带逗号，否则不是tuple类型
# t4 = ('one',)
# print(f"t4的类型是：{type(t4)},内容是：{t4}")
# # 元组的嵌套
# t5 = (1,2,3,t4,(6,7))
# print(f"t5的类型是：{type(t5)},内容是：{t5}")
# # 元组也可以利用下表索引取出元素 取出 t5中的7
# element = t5[4][1]
# print(f"从嵌套t5中取出的数据是：{element}")

# # 元组的操作：index查找方法
# t6 = ('Cancer','bear','resg')
# index = t6.index('bear')
# print(f"在元组t6中查找bear，的下标是：{index}")
# # 元组的操作：count统计方法
# t7 = ('Cancer','bear','resg',2,2,1)
# count = t7.count(2)
# print(f"元组t7中有{count}个2")
# # 元组的操作：len函数统计元组的元素数量
# t8 = ('Cancer','bear','resg',2,0,1)
# sum = len(t8)
# print(f"元组t8中有{sum}个元素")
# # 元组的遍历：while
# index = 0
# while index < len(t8):
#     element = t8[index]
#     print(f"通过while遍历的元组有元素：{element}")
#     index += 1
#
# # 元组的遍历：for
# for element1 in t8:
#     print(f"通过for遍历的元组有元素：{element1}")
# # 修改元组内容：
# # t8[0] = 'sad'
# 修改元组中嵌套的list内容
t9 = (1,2,["hello",'mk'],'iji')
print(f"t9的内容是：{t9}")
t9[2][0] = '你好'
print(f"修改后t9的内容是：{t9}")