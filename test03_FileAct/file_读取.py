"""
演示对文件的读取
"""
import time

# 打开文件
f = open("D:\Test\Python_test.txt","r",encoding="UTF-8")
print(type(f))
# 读取文件 - read()
print(f"read读取10个字节结果是：{f.read(10)}")
print(f"read读取全部字节结果是：{f.read()}") # 连续调用read会从上一个read的结尾处开始
# 读取文件 - readlines()
lines = f.readlines() # 读取文件的全部行 封装到列表中
print(f"lines的对象类型是：{type(lines)}")
print(f"lines对象内容是：{lines}") # 文件读取就想有个小指针记录读取的位置
# 读取文件 - readline()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")
# for循环读取文件行
for line in f:
    print(f"每一行数据：{line}")
# 文件的关闭 close()
# time.sleep(30)
f.close()
# with open语法操作文件
with open("D:\Test\Python_test.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)

