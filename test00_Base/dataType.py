# 使用type()查看数据类型
print("2211.222的数据类型",type(2211.222))
print("2211的数据类型",type(2211))
print("stwiuy的数据类型",type("stwiuy"))
# 另一种写法
int_type=type(2211.222)
float_type=type(2211)
string_type=type("stwiuy")
print(int_type,float_type,string_type)
name="puppy"
print(type(name))

# 数据类型转换
# 使用str()将int/float转换为string
num_string=str(11)
print(type(num_string),num_string) # 类似的，float也可以转为string
# 将string转为int 只有字符串全部包括数字才能成功，否则运行报错
# 错误示例
#string_number=int("it's your fault")
#print(type(string_number),string_number)
# int可以转为float，float转int可能会丢失精度
float_int=int(12.99)
print(type(float_int),float_int)
