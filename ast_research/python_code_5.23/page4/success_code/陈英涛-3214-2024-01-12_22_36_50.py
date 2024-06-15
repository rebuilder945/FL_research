lst  =eval(input())
a=lst.count(0)
lst1 = []
for i in lst:
    if i!=0:
        lst1.append(i)
lst2 = lst1+[0]*a
print(lst2)
