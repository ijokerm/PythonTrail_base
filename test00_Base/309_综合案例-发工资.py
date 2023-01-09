import random
# 账户1W 给20个员工发工资
#员工编号1-20 依次发放 每人可领取1000
#领工资根据绩效 1-10（随机生成），低于5 不发工资，换下一位
#如果工资发完结束发工资
money = 10000

for i in range(1,21):
    flag = random.randint(1, 10)
    print(f"员工{i},",end='')
    if flag < 5:

        print(f"当前余额{money}，绩效分{flag}，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"当前余额{money}，绩效分{flag},发工资，下一位")
    else :
        print(f"当前余额{money}，不发了，下个月再来")
        break

