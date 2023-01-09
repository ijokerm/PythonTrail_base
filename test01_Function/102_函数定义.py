# # 定义一个简单的函数
# def say_hi():
#     print("hi,everbody.It's Vivian")
#
# # 定义好函数，，要使用必须要调用它
#
# say_hi()
# 案例自动查核酸
# def check_f():
#     print("欢迎来游乐园！\n请出示您的的健康码以及72小时核酸证明！")
#
# check_f()
# 传参函数 两数相加
def add(x,y):
    re = x + y
    print(f"{x}和{y}的和为{re}")
# 调用函数，传入要计算的两个数字
add(12333,23321)

# 传参函数案例 定义一个函数，名称不限定，接受一个参数传入（数字类型，表示体温）
# 在函数内进行体温判断 判断值 37.3度
def check_t(data:float):
    print("欢迎来到游乐园，请出示您的的健康码以及72小时核酸证明，并配合测量体温！")
    if data <= 37.3:
        print(f"体温测量中，您的体温是{data},体温正常请进！")
    else :
        print(f"体温测量中，您的体温是{data},需要隔离！")

check_t(37.4)

