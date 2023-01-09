# 定义一个元组 记录学生姓名 年龄 爱好
t = ('Jay',11,['football','music'])
# 查询年龄所在下标位置
index = t.index(11)
print(f"年龄所在下标位置为：{index}")
# 查询学生的姓名
name = t[0]
print(f"学生姓名为：{name}")
# 删除学生爱好中的football
pop_t = t[2].pop(0)
print(f"删除{pop_t}后元组的元素有：{t}")
# 增加爱好 coding 到爱好list内
ins_t = t[2].append('coding')
print(f"增加coding到元组后元素有：{t}")
