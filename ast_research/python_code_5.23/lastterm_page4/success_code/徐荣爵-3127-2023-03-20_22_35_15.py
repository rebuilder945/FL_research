n = int(input())
lst = [x for x in range(1,n+1)]
lst2 = []
for i in range(n-1):
    m = int(i)+2
    lst2.append(m)
lst2.append(1)
print(lst2)
