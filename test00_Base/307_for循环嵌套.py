# # for嵌套
# # 每天表白，坚持100天，每天送10朵花
# i = 0
# for i in range(1,101):
#     print(f"今天是向小美表白的第{i}天。")
#     # 内层控制送花
#     for j in range(1,11):
#         print(f"给小美送的第{j}朵花")
#     print("我喜欢你，小美")
# print(f"第{i}天，表白成功")

# for循环实现九九乘法表
for i in range(1,10):  # 外层控制行
    for j in range (1,i+1):  # 内层控制每一行输入内容
        print(f"{j}*{i}={j*i}\t",end='')
    print()

