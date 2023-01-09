# 定义一个简单的函数 作为自定义模块--演示自定义模块导入
def test(a,b):
    print(a+b)
# 只在当前模块中调用该函数
if __name__ == '__main__':
    test(1, 3)