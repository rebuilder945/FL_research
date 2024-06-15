lst=eval(input())
lst1=[]
lst2=[max(lst),min(lst)]
for x in lst:
    if x not in lst2:
        lst1.append(x)
print(lst1)
