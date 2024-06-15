lst=eval(input())
if 0 in lst:
    lst.remove(0)
if 1 in lst:
    lst.remove(1)
lst1=lst.copy()
for x in range(len(lst)):
    for i in range (2,lst[x]):
        if lst[x]%i==0:
            lst1.remove(lst[x])
print(lst1)
    
