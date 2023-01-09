# # 局部变量：
# def test_a():
#     num = 100
#     print(num)
# # 调用test_a
# test_a()
# print(num)
#
# 在函数内修改全局变量
# num = 200
# def test_a():
#     print(f"test_a:{num}")
#
# def test_b():
#     num = 400  # 局部变量
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)

# 借助global关键字 --在函数内修改全局变量
num = 200
def test_a():
    print(f"test_a:{num}")

def test_b():
    global num # 将内部定义的变量变为全局变量，等同于外面的num
    num = 400
    print(f"test_b:{num}")

test_a()
test_b()
print(num)