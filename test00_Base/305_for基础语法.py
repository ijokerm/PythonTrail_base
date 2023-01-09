# #定义变量
# name = "springbear"
# #使用for循环遍历
# for X in name:
#     # 将变量name中的内容挨个取出赋予X临时变量
#     print(X,end='')
# 练习 数一数字符串中有几个a
# 定义字符变量
name = input()
flag = input()
# 定义一个计数变量
count = 0
for X in name:
    if X == flag:
        count += 1
print(f"{name}中含有：{count}个{flag}")
