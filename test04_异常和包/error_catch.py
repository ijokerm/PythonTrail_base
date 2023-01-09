"""
演示捕获异常
"""
# # 基本捕获语法
# try:
#     f = open("D:/Test/error.txt", 'r', encoding='UTF-8')  # 读取一个不存在的文件，运行出现异常FileNotFoundError
# except:
#     print("出现异常，因为文件不存在。我将open模式由r--w")
#     f = open("D:/Test/error.txt", 'w', encoding='UTF-8')
# # 捕获指定异常
# try:
#     print(nana)
#     # 1 / 0
# except NameError as n:
#     print("出现了变量未定义的异常")
#     print(n) # 其中n记录异常的具体
# # 捕获多个异常
# try:
#     29 / 0
# except (NameError,ZeroDivisionError) as e:
#     print("出现了变量未定义或者除以0的异常",e)
# # 未正确设置捕获异常类型，将无法捕获异常

# 捕获所有异常
try:
    f = open("D:/Test/fin.txt",'r',encoding='UTF-8')
except Exception as e:
    print("出现异常了",e)
    f = open("D:/Test/fin.txt",'w',encoding='UTF-8')
else:
    print("没有异常继续执行")
finally:
    print("在finally，有没有异常都要执行,一般用于最后关闭资源")
    f.close()
