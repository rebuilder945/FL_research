lst=eval(input())
lstcopy=lst.copy()
a=lst.county(0)
for x in lst:
    if x==0:
        lstcopy.remove(x)
for y in range(x):
    lstcopy.append(0)
print(lstcopy)
