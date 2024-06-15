name_list = input().split(",")
score_list = list(map(int, input().split(",")))
# zip函数可以将两个列表按照相同下标的元素配对形成元组
student_list = list(zip(name_list,score_list))
# 按照列表中第二个元素即分数进行排序
student_list.sort(key=lambda x:x[1])

print(student_list)

