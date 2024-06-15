from itertools import combinations


name = input().split('')
grade = eval(input())
comb = []
for i in range(len(grade)):
    ls = []
    ls.append(name[i])
    ls.append(grade[i])
    comb.append(ls)
print(comb)

