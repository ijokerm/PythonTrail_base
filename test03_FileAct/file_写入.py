# # 打开一个并不存在的文件 --创建
# with open('D:/Test/write.txt',"w",encoding='UTF-8') as f:
#     f.write("hello puuoo") # close()方法内置了flush()

# 打开已经存在的write.txt
f = open("D:/Test/write.txt","w")
f.write(f"重新写入的内容{staticmethod}")
