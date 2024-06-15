StudentList1 = input().split(',')
StudentList2 = input().split(',')

# eval() 函数用于执行以字符串形式给出的表达式或语句。
# 它接受三个参数：eval(expression, globals=None, locals=None)，
# 其中 expression 是要评估的字符串，globals 和 locals 是可选的字典，指定了全局和局部命名空间，
# 但在代码中，试图将 set(StudentList1) 和 set(StudentList2) 的结果作为 eval() 函数的参数
StudentSet1 = set(StudentList1)
StudentSet2 = set(StudentList2)

# 计算交集和并集
set1 = StudentSet1 & StudentSet2  # 得到同时出现在两份名单中的人
set2 = StudentSet1 | StudentSet2  # 得到两份名单中的所有人

print(sorted(list(set1)))
print(sorted(list(set2)))

