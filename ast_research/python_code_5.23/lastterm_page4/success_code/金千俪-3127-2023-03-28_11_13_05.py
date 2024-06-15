a=int(input())
lst=[a*1 for a in range(1,a+1)]
for a in range(a):
    lst.insert(len(lst),lst[0])
    del lst[0]
    break
print(lst)
