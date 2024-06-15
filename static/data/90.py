StudentList1 = input().split(',')
StudentList2 = input().split(',')

StudentSet1 = set(StudentList1)
StudentSet2 = set(StudentList2)
# append() 方法会在原列表上进行操作，并且返回值为 None，
# 因此 StudentSet1 和 StudentSet2 都被赋值为 None，而不是预期的集合，
# 可以分开操作，先将两个列表合并，然后再转换为集合。

set1 = StudentSet1 & StudentSet2
set2 = StudentSet1 | StudentSet2

print(sorted(list(set1)))
print(sorted(list(set2)))