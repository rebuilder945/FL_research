StudentList1 = input().split(',')
StudentList2 = input().split(',')
StudentSet1, StudentSet2 = set(StudentList1), set(StudentList2)
#对列表进行这种操作是不支持的，因为 ^ 是集合操作符，用于计算两个集合的对称差集，而不是列表
set1 = StudentSet1 ^ StudentSet2 
set2 = StudentSet1 | StudentSet2 
print(sorted(list(set1)))
print(sorted(list(set2)))