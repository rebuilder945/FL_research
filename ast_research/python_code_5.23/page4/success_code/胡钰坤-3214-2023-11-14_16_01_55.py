# ls = eval(input())
# for i in range(len(ls)):
#     if ls[i] == 0:
#         j = i + 1
#         while j < ls(len(ls)):
#             if ls[j]!=0:
#                 ls[i] = ls[j]
#                 ls[j] = 0
#                 break
#             j = j + 1
# print(ls)

ls1 = eval(input())
ls2 = ls1.copy()
for x in range(len(ls2)):
    cnt = ls2.count(0)
    for i in range(cnt):
        ls1.remove(0)
        ls1.append(0)
print(ls1)
        
