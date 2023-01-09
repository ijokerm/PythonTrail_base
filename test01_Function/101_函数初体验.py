# 不使用内置函数 求字符串的长度
str1 = 'jsonkij'
str2 = 'fgrye789pp'
str3 = 'gh yy'

count = 0
for i in str1 :
    count += 1
print(f"字符串str1的长度为{count}")

count = 0
for i in str2 :
    count += 1
print(f"字符串str2的长度为{count}")

count = 0
for i in str3 :
    count += 1
print(f"字符串str3的长度为{count}")

# 以上代码非常重复低效，使用函数来优化
# 已组织好的、可重复使用，针对特定功能
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)