# 将内容写入记事本，复制保存到；word.txt 存到D:\Test\word.txt
# 通过文件读取操作 读取文件 并统计bear 出现的次数
with open("D:\Test\word.txt","r") as f:
   # 方法1 利用for循环一行行读取--一步步操作较为麻烦
    # count = 0
    # for line in f:
    #     line = line.strip()#去除每行结尾换行符\n
    #     line = line.replace(',',' ')
    #     line = line.replace('.', ' ')
    #     tmp = line.split(' ')
    #     print(tmp)
    #     for tmp2 in tmp:
    #         if tmp2 == 'bear':
    #             count += 1
    # print(f"bear出现的次数：{count}")
  # 方法2 读取全部内容--str类型，通过count直接统计
    comtent = f.read()
    count = comtent.count('bear')
    print(comtent,type(comtent),count)