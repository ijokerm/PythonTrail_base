"""
 已有一份账单文件，需求:读取文件，将文件写入备份，将文件内标记为测试的数据丢弃
"""
# open r模式 打开文件对象读取
f = open("D:/Test/bill.txt","r",encoding="UTF-8")
# open w 准备备份文件 用于文件写出
bak = open("D:/Test/bill_bak.txt",'w',encoding='UTF-8')
for line in f:
    line = line.strip() # 去掉换行
    tmp = line.split(',')
    if tmp[4] == '测试':
        continue
    # 将内容写入 ，不要忘记之前进行了strip() 最后要把换行加上
    bak.write(line)
    bak.write('\n')
# for循环 判断是否标记测试 不是就write写出 是的话continue跳过
f.close()
bak.close() 

# 关闭两个文件