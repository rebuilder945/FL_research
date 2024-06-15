sName = input().split(",")
sGrade = eval(input())
lst = []
for i in range(len(sName)):
    lst.append([sName[i],sGrade[i]])
print(lst)
#错误

# sName = input().split(",")
# sGrade = eval(input())
# lst2 = []
# for i in range(len(sName)):
#     lst = ()
#     lst=([sName[i],sGrade[i]])
#     lst2.append(lst)
# print(lst2)
#正确

