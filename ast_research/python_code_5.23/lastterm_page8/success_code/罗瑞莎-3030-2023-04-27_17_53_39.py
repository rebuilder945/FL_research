names = input().split(',')
scores = input().split(',')
scores1 = list(map(int,scores))
scores2 = scores1.copy()
scores2.sort()
lst = []
lst1 = []
for i in scores2:
    lst1.append(names[scores1.index(i)])
    lst1.append(i)
    lst.append(lst1)
    lst1 = []
print(lst)
