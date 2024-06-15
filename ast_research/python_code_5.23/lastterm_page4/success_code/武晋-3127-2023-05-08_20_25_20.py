n=int(input())
lst=[x for x in range(1,n)]
for x in lst:
    lst.remove(x)
    lst.append(x)
print(lst)



