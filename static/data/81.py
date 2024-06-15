StudentList1 = input().split(',')
StudentList2 = input().split(',')
StudentSet1 = set(StudentList1)
StudentSet2 = set(StudentList2)#想要创建两个不同的集合，因此需要分别使用 set() 函数。
set1 = StudentSet1 & StudentSet2
set2 = StudentSet1 | StudentSet2
print(sorted(list(set1)))
print(sorted(list(set2)))