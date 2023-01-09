# if-elif-else简单练习

# print("欢迎来到本游乐场。")
# height = int(input("请输入你的身高(cm): "))
# vip_level = int(input("请输入你的VIP等级(1-5): "))
#
# # if判断--第一个条件
# if height <= 120 :
#     print("身高不超过120，可以免费游玩。")
# elif vip_level > 3:
#     print("VIP级别大于3，可以免费游玩。")
# else :
#     print("您需要买票20元。")
#
# print("祝您游玩愉快。")

# 简洁版本：去掉变量的使用，直接将input()写入判断条件中--按顺序要求输入满足条件则执行完毕
if int(input("请输入你的身高(cm): ")) <= 120 :
    print("身高不超过120，可以免费游玩。")
elif int(input("请输入你的VIP等级(1-5): ")) > 3:
    print("VIP级别大于3，可以免费游玩。")
elif int(input("请输入今天几号: ")) == 1:
    print("今天是免费游玩日，教可以免费游玩。")
else :
    print("您需要买票20元。")  # 最终else可去

print("祝您游玩愉快。")
