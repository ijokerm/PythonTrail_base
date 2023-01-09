"""
自定义模块实现文件处理功能
"""

def print_file_info(file_name):
    """
    接收文件传入的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
    :param file_name:
    :return:
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        content = f.read()
        print(content)
    except Exception as e:
        print("文件出现异常：",e)
    finally: # 假如文件内容不存在，则f内容为空,不再是文件类型，使用f.close()会报错 需要加个判断
        if f: # 如果f是None表示False f有内容则是True
            f.close()

def append_to_file(file_name,data):
    """
    接收文件路径以及传入数据，将数据追加写入到文件中
    :param file_name:
    :param data:
    :return:
    """
    f = open(f"{file_name}", 'a', encoding='UTF-8')
    f.write(data)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    # print_file_info("D:/Test/bill.txtw")
    append_to_file('D:/Test/apend.txt',"ff")