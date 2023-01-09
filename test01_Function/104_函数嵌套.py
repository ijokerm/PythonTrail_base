# 函数嵌套
def fun1():
    print("--2--")

def fun2():
    print("--1--")
    # 嵌套调用fun1
    fun1()
    print("--3--")
# 调用fun2
fun2()