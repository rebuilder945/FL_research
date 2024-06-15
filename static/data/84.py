StudentList1 = input().split(',')
StudentList2 = input().split(',')
StudentSet1 = set(StudentList1)
StudentSet2 = set(StudentList2)#StudentSet1 和 StudentSet2 被直接赋值为了 StudentList1 和 StudentList2，而它们本身应该是集合类型
set1 = StudentSet1 & StudentSet2
set2 = StudentSet1 | StudentSet2
print(sorted(list(set1)))
print(sorted(list(set2)))