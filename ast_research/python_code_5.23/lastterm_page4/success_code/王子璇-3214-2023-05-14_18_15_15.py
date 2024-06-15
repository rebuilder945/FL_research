lst=eval(input())
lstcopy=lst.copy()
a=lst.count(0)
for x in lst:
    if x==0:
        lstcopy.remove(x)
for y in range(a):
    lstcopy.append(0)
print(lstcopy)
