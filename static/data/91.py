StudentList1 = input().split(',')
StudentList2 = input().split(',')

combined_list = StudentList1 + StudentList2
#insert() 方法用于在列表中的指定位置插入一个元素，但它需要两个参数：要插入的索引位置和要插入的值。

StudentSet1 = set(combined_list)
StudentSet2 = set(combined_list)

set1 = StudentSet1 & StudentSet2  # 得到同时出现在两份名单中的人
set2 = StudentSet1 | StudentSet2  # 得到两份名单中的所有人

print(sorted(list(set1)))
print(sorted(list(set2)))