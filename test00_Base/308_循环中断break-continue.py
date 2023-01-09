# # 演示continue语法以及输出
# for i in range(1,5):
#     print("语句1")
#     continue
#     print("语句2")  # 因为continue将该语句中断

# # 演示continue语法嵌套以及输出
# for i in range(1,5):
#     print("语句1",end='')
#     for j in range(1,3):
#         print("语句2",end='')
#         continue
#         print("语句3",end='')
#     print("语句4")

# 演示break语法以及输出
# for i in range(1,5):
#     print("语句1")
#     break
#     print("语句2")  # 因为遇到break整个循环中断
# print("语句3")

# 演示break语法嵌套以及输出
for i in range(1,5):
    print("语句1",end='')
    for j in range(1,3):
        print("语句2",end='')
        break
        print("语句3",end='')
    print("语句4")