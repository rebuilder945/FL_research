StudentList1 = input().split(',')
StudentList2 = input().split(',')
StudentSet1 = set(StudentList1)
StudentSet2 = set(StudentList2)#使用 set() 函数来创建实际的集合对象。
set1 = StudentSet1 & StudentSet2
set2 = StudentSet1 | StudentSet2 
print(sorted(list(set1)))
print(sorted(list(set2)))