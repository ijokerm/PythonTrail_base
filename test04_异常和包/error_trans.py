"""
演示异常的传递性
"""
# 定义一个出现异常的方法-函数
def func01():
     print("func01开始执行")
     num = 1 / 0 # 有异常
     print("func01结束执行")
# 定义一个没有异常的方法 调用上面的方法
def func02():
    print("func02开始执行")
    func01()
    print("func02结束执行")
# 定义一个方法调用第二个没有异常的方法
def main(): # 在这里处理异常
    try:
        func02()
    except Exception as e:
        print("出现异常了",e)

main()