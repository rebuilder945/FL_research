lst1=eval(input())
lst2=[]
for x in lst1:
    if lst1.count(x)==1:
        lst2.append(x)
lst2.sort(reverse=False)

if lst2==[]:
    print(','.join(str(i) for i in lst2))
else:
    print(lst2)
