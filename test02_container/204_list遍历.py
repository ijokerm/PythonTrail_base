# 利用while循环 遍历列表list
def list_while():
    """
    演示while遍历list
    :return:None
    """
    my_list = ['use','fire','faith','python']
    # 循环控制变量通过下标索引来控制 默认0
    # 每一次循环将下标索引+1
    # 循环条件：下标索引变量 < 列表的元素数量
    index = 0
    while index < len(my_list):
        # 通过index变量取出下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1 # 至关重要 index每次循环+1

# 利用for循环遍历列表list
def list_for():
    """
    演示for遍历list
    :return:None
    """
    my_list = [1,2,3,4,5,6]
    # for 临时变量 in 数据容器:
    for element in my_list:
        print(f"列表的元素有：{element}")
# list_while()
# list_for()

# 遍历案例 定义一个列表 取出其中的偶数 并存入一个新的列表 while/for 各自实现
def test_while():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    index =0
    res_list = list()
    while index < len(my_list):
        element = my_list[index]
        if element % 2 == 0:
            res_list.append(element)
        index += 1
    print(res_list)

def test_for():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res_list = list()
    for element in my_list:
        if element % 2 == 0:
            res_list.append(element)
    print(res_list)

# test_while()
test_for()