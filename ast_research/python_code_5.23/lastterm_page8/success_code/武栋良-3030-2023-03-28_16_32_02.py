lst1 = input().split(',')
lst2 = list(map(int,input().split(',')))
lst = []
n = len(lst2)
for i in range(n):
    a = [lst1[i],lst2[i]]
    lst.append(a)
print(sorted(lst,key=(lambda x:x[1])))


