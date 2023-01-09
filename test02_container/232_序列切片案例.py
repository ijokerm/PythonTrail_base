# 将字符串 万过薪月，熊的天春，nohtyP学 提取出 春天的熊
# 方法1 倒序后切片
my_str = "万过薪月，熊的天春，nohtyP学"
new_str = my_str[::-1]
res = new_str[8:12]
print(res)
# 方法2 切片后倒序
my_str = "万过薪月，熊的天春，nohtyP学"
new_str = my_str[5:9]
res = new_str[::-1]
print(res)
# 方法3 使用split分割 ，再利用replace替换“来”为空 最后逆序
my_str = "万过薪月，熊的天春来，nohtyP学"
new_str_list = my_str.split("，")[1].replace("来","")
#tmp = new_str_list[0]
res = new_str[::-1]
print(res)