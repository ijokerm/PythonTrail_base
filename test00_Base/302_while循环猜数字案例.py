# 设置1-100范围的随机数，通过while循环配合input判断输入的数字是否相等
import random
num = random.randint(1,100)
# 定义变量记录猜测的次数
count =0
# 定义一个bool类型的变量，作为是否继续循环的标记
flag = True
while flag:
    guess_num = int(input("请输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("恭喜你，猜对啦")
        # 利用flag来终止循环
        flag = False
    else :
        if guess_num < num:
            print("猜小了")
        else :
            print("猜大了")
print(f"你猜测了{count}次")
