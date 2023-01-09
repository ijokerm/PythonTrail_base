# 从后向前看，每天剩余桃子的数量加上1再乘以2就是前一天桃子的数量。
num=1
for i in range(4):
    num=(num+1)*2
print(num)