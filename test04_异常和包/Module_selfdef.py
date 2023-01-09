"""
演示自定义模块
"""
# # 导入自定义模块使用
# import test_1.my_module1 as test
# # 导入不同模块的同名功能
# # import test_1.my_module2 as test
# test.test(1,2)
# # __main__

# __all__
from test_1.my_module2 import  *
test_B()
test_A()