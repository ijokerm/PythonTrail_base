# 定义一个和test同名的函数 --演示自定义模块导入同名功能
__all__ = ['test_B']

def test_A(a,b):
    print(a - b)

def test_B(a,b):
    print(a + b)
