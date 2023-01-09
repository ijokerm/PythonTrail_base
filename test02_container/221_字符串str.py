"""
以数据容器--再识字符串
"""
my_str = "it is my chance to success"
# 通过下标索引取值
val1 = my_str[3]
val2 = my_str[-3]
print(f"取下标为3和-3的元素值分别为：{val1},{val2}")

# 修改第一个i--I
# my_str[0] = "I"
# index方法 查找my的起始下标
index = my_str.index('my')
print(f"my的起始下标:{index}")
# replace方法 将it--It  replace方法并没有修改字符串本身，而是得到了一个新的字符串
new_str = my_str.replace('it','It')
print(f"{my_str}替换后字符串：{new_str}")
# split 方法
my_str = "hello my cute piggy"
my_slist = my_str.split(" ")
print(f"字符串{my_str}按照空格进行切割后得到：{my_slist},类型是{type(my_slist)}")
# strip 方法 不传参（默认去除前后空格）/传参
my_str = "  i miss my piggy   "
new_str = my_str.strip()
print(f"{my_str}做strip默认不传参得到：{new_str}")
my_str = "122i miss my piggy211 "
new_str = my_str.strip('12')
print(f"{my_str}做strip传参得到：{new_str}")
# 统计字符串中某字符 出现次数,count
my_str = "I miss my piggy." # 统计‘i’出现的次数
count = my_str.count('i')
print(f"'i'在字符串{my_str}中出现的次数为：{count}") # 区分大小写
# 统计字符串长度，len()
my_str = "I miss my piggy." # 统计‘i’出现的次数
sum_s = len(my_str)
print(f"{my_str}的长度是：{sum_s}")
