lst1 = eval(input())
lst=[]
for i in lst1:
    if not i in lst:
        lst.append(i)
for a in lst:
    for x in range(lst1.count(a)-1):
        lst1.remove(a)
    
print(lst1)


