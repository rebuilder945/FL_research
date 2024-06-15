lst=eval(input())
lst1=[]
for x in lst:
    if x!=2 and x%2==0:
        lst1.append(x)
    if x==2:
        lst1.append(x)
    else:
        pass
print(lst1)
