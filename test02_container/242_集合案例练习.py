# 有如下列表对象：
my_list = ['春天的熊','joker','bear','coding','python','sHSb','sHSb']
# 定义一个空集合
my_set = set()
# 通过for循环遍历列表
for element in my_list:
    my_set.add(element)
print(f"去重后集合对象：{my_set}")
# 在for循环中将列表中的元素添加至集合
# 最终得到去重后的集合额对象 打印输出