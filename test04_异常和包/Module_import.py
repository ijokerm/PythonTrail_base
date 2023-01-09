"""
演示模块导入
"""
import time  # 使用import 导入time模块使用sleep()功能
print("暂停5秒后开始")
time.sleep(5)  # 通过 模块. 就可以使用模块内部的全部功能
print("开始")
# 使用from导入time的sleep 只用其中的一个功能
from time import sleep
print("暂停5秒后开始")
sleep(5)
print("开始")
# 使用 * 导入time模块的全部功能
from time import *
print("暂停5秒后开始")
sleep(5)
print("开始")
# 使用as给特定功能加上别名
import time as t
print("暂停5秒后开始")
t.sleep(5)
print("开始")
from time import sleep as sl
print("暂停5秒后开始")
sl(5)
print("开始")

