# # 演示使用多个变量 接收多个返回值
# def test_return():
#     return 1,'hhh',False
#
# x, y ,z = test_return()
# print(x)
# print(y)
# print(z)

# # 演示多种传参的形式
# def user_info(name,age,gender):
#     print(f"姓名是{name},年龄是{age},性别是{gender}")
#
# # 位置参数 -默认使用形式 传递的参数和定义的参数顺序及个数必须一致
# user_info('piggy',24,'男')
# # 关键字参数 -参数之间不存在先后顺序
# user_info(name='doggy',age=23,gender='男')
# user_info(age=23,name='doggy',gender='男')
# user_info('bear',age=23,gender='女')
# # 缺省参数（默认值）-不传就按默认值，传了就覆盖默认值 注意默认的参数必须写在最后
# def user_info(name,age,gender='男'):
#     print(f"姓名是{name},年龄是{age},性别是{gender}")
# user_info('Tom',23)
# # 不定长 -位置不定长 * 形参作为元组存在接收不定长数量的参数传入
# def user_info(*args):
#     print(f"args参数的类型是：{type(args)},内容是：{args}")
# user_info(1,2,3,'nana')
# # 不定长 -关键字不定长 **
# def user_info(**kwargs):
#     print(f"args参数的类型是：{type(kwargs)},内容是：{kwargs}")
# user_info(k1=1,name='baby',k3='ew')
"""
匿名函数：1.函数作为参数传递；2.lambda函数
"""
# 定义一个函数，接收另一个函数作为传入参数
def test_func(compute):
    res = compute(1,2) #确定compute是函数
    print(f"compute参数的类型：{type(compute)}\n计算结果：{res}")
# 定义一个函数 准备作为参数传入另一个函数
def compute(x,y):
    return x+y
# 调用 并传入参数
test_func(compute)

# 通过lambda匿名函数的形式，将匿名函数作为参数传入
test_func(lambda x,y:x+y) # 只能用一次，但是很简洁