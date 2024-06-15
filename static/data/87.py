StudentList1 = input().split(',')
StudentList2 = input().split(',')
# 将列表转换为集合,集合的元素是可哈希
StudentSet1 = set(StudentList1)
StudentSet2 = set(StudentList2)

set1 = StudentSet1&StudentSet2
set2 = StudentSet1|StudentSet2
print(sorted(list(set1)))
print(sorted(list(set2)))

