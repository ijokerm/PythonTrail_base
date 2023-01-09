# # 语法1 range(num)
# for X in range(10):
#     print(X)

# 语法2 range(num1,num2)
# for X in range(2,5):
#     print(X)
#     # 从2开始到5结束，不包含5本身 -一个数字序列

# 语法3 range(num1,num2,step)
for X in range(2,10,2):
    print(X)
    # 从2开始到10结束，不包含5本身并且步长为2-数字间隔为2
print(X) # 有警告但是没有报错，可以运行，但是不符合代码规范

# # 练习案例-求有多少个偶数
# num = 100
# count = 0
# for X in range(1,num):
#     if X % 2 == 0:
#         count += 1
# print(f"1-{num}(不含109)范围内，有{count}个偶数")

