StudentList1 = input().split(',')
StudentList2 = input().split(',')

sorted_StudentList1 = sorted(StudentList1)
sorted_StudentList2 = sorted(StudentList2)

StudentSet1 = set(sorted_StudentList1)
StudentSet2 = set(sorted_StudentList2)

#对两个列表进行排序，然后再创建集合并执行交集和并集操作
set1 = StudentSet1 & StudentSet2
set2 = StudentSet1 | StudentSet2

print(sorted(set1))
print(sorted(set2))