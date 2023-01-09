num=1021
salary=11000
out="python自动化测试，第%s期，薪资%s" %(num,salary)
print(out)


# %s转为字符串放入占位
# %d转为整数
# %f转为浮点型
sid=12121
name="jioo"
kpi=2222.3333
out="员工号为%d,姓名为%s,KPI绩效考核数值如下\n %f" %(sid,name,kpi)
print(out)
# 精度控制 sid控制为8位，KPI控制为8位小数精度位2
print("sid宽度限制为8，sid=%8d" %sid+"kpi宽度限制为8小数精度为2，kpi=%8.2f"%kpi)
#更快速的格式化方式 f"内容{变量}" f-format（格式化   ）
out1=f"员工号为{sid},姓名为{name},kpi绩效考核数值如下\n {kpi}"
print(out1) # 不限数据类型也不做精度控制

# 格式化 表达式--一条具有明确执行结果的代码语句 等号右侧
print("1*1 的结果是：%d" %(1*1))
print(f"1*1 的结果是：{1*1}")
print("字符串在Python中的类型是：%s" %(type('字符串')))





