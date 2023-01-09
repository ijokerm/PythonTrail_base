# 定义一个函数 完成两数相加 并且通过返回值将相加的结果返回给调用者
def add(x,y):
    """
    说明函数作用：
      :param x:形参1
      :param y:形参2
      :return:两数相加的和
    """
    return x + y
    print("ffjj") # 不会执行--函数体遇到return关键字，表明函数在此结束了 之后的内容不会执行
re = add(21,132)
print(re)

# def say_hi():
#     print("hikk")
#
# re=say_hi()
# print(f"无返回值函数，返回内容是{re}")
# print(f"无返回值函数，返回内容的类型是{type(re)}")

# # return None --使用场景1.结合if判断
# def check_a(age):
#     if age >= 18:
#        # print("SUCCESS")
#         return "SUCCESS"
#     else:
#         return None
# res = check_a(11)
# print(res)
# if res == None:
#     print("未成年，禁止出入网吧")
#
# # return None --使用场景2.用于声明无内容的变量