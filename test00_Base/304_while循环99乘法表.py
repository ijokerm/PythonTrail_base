# print("hello\tworld")
# print("itYYYY\tpractice")
# while实现九九乘法表
# 外层控制行 内层控制行的内容
i = 1
while i <= 9:

    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')
        j += 1
    i += 1
    print()