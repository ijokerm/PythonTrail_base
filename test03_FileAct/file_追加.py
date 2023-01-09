"""
演示文件追加
"""
import time

# # 打开（创建）一个不存在的文件
# f = open("D:/Test/test_1.txt",'a',encoding='UTF-8')
# # 写入内容
# f.write("learn 'a' model.")
# # 刷新
# f.flush()
# # 关闭
# f.close()

# 打开一个已存在的文件
f = open("D:/Test/test_1.txt",'a',encoding='UTF-8')
f.write("\n换行写入")
# 关闭 close()内置有flush()
f.close()