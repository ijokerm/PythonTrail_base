# # 给定一个字符串
# my_str = "I will never give up"
# # 1.统计字符串内某字符 ‘i’
# count = my_str.count('i')
# print(f"{my_str}内‘i'的个数为：{count}")
# # 2.将字符串内的空格替换为‘|’
# new_str = my_str.replace(' ','|')
# print(f"{my_str}替换后为{new_str}")
# # 3.按照‘|’进行分割得到list
# new_list = new_str.split("|")
# print(f"{new_str}按照|分割后，得到{new_list}")
# # strip
# str1 = "|ij|jjjj,dd |"
# str = str1.strip("|")
# print(str1,str)

# while/for遍历
my_str = "it's a trap"
index = 0
while index < len(my_str):
    element = my_str[index]
    print(f"while遍历{my_str}内的元素：{element}")
    index += 1
for element in my_str:
    print(f"for遍历{my_str}内的元素：{element}")