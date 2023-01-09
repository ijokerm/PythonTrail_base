"""
演示数据容器--list
语法[元素,元素,元素...]
"""
# # 定义一个列表list
# my_list = ["bear",12,'python']
# print(my_list)
# print(type(my_list))
# # 元素类型无限制
# my_list = ["bear",12,True]
# print(my_list)
# print(type(my_list))
# # 定义一个嵌套列表
# my_list = [["1",'2'],[12,32],True]
# print(my_list)
# print(type(my_list))

# 通过下标索引来取出对应位置的数据 正向
my_list = ['tom','lily','rose']
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 错误示范-->通过索引下标取数据一定不能超出索引范围--否则会报错：IndexError: list index out of range
# print(my_list[3])
# 通过下标索引来取出对应位置的数据 反向
print(my_list[-1])  # rose
print(my_list[-2])  # lily
print(my_list[-3])  # tom
# 取出嵌套列表中的元素 先外后内
my_list = [["1",'2'],[12,32],True]
# 取出[12,32]中的32
print(my_list[1][1])