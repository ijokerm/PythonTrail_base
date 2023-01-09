"""
模块实现字符串相关工具：
"""

def str_reverse(s):
    """
    接受传入的字符串，将字符串反转返回
    :param s:
    :return:
    """
    restr = s[::-1]
    return restr

def substr(s,x,y):
    """
    按照下标x,y对字符串进行切片
    :param s:
    :param x:
    :param y:
    :return:
    """
    restr = s[x:y]
    return restr

if __name__ == '__main__':
    str = '春天的熊bera'

    print(str_reverse(str))
    print(substr(str,0,1))