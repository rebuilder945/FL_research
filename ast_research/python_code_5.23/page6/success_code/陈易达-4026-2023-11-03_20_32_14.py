n = eval(input())
list1 = [1,2]
for x in range(n-2):
    list1.append(list1[x]+list1[x+1])
list2 = [2,3]
for x in range(n-2):
    list2.append(list2[x]+list2[x+1])
ls = []
for x in range(n):
    y = list2[x]/list1[x]
    ls.append(y)
s = sum(ls)
print('%.4f'%s)
