# 实现ATM
# 定义一个全局变量，记录银行卡余额
money = 5000000
# 定义一个全局变量，记录客户姓名（程序启动时输入）
name = input("请输入您的姓名：")
# 定义如下函数:
# 1、查询余额函数
def check_m(show_header):
    if show_header:
        print("----------------查询余额--------------")
    print(f"{name}，您好，您的余额剩余：{money}元。\n")

# 2、定义存款函数
def save_m(num):
    global money # 将money在函数内部定义为全局变量，可修改值
    money += num
    print("----------------存款-----------------")
    print(f"{name}，您好，您存款50000元成功")
    check_m(False)  # 调用查询函数来查询

# 3、定义取款函数
def get_m(num):
    global money
    money -= num
    print("----------------取款-----------------")
    print(f"{name}，您好，您取款50000元成功")
    check_m(False)  # 调用查询函数来查询

# 4、主菜单函数：
def main_m():
    print("-----------------主菜单----------------")
    print(f"{name}，您好,欢迎来到bearATM,请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

# 设置无限循环，确保程序不会退出
while True:
    key_bord=main_m()
    if key_bord == "1":
        check_m(True)
        continue # 确保查询余额、取款、存款后返回主菜单
    elif key_bord == "2":
        save_num = int(input("您想要存多少钱？请输入："))
        save_m(save_num)
        continue
    elif key_bord == "3":
        get_num = int(input("您想要取多少钱？请输入："))
        if get_num > money:
            print("余额不足！")
        else:
            get_m(get_num)
        continue
    else:
        print("程序退出啦！")
        break # 通过break跳出循环 退出

