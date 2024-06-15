StudentList1 = input().split(',')
StudentList2 = input().split(',')
StudentSet1,StudentSet2 = set(Students1),set(Students2)
set1 = Students1&Students2#得到同时出现在两份名单中的人
set2 = StudentSet1|StudentSet2 #得到两份名单中的所有人
print(sorted(list(set1)))
print(sorted(list(set2)))

