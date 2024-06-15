a=int(input())
lst1=[i for i in range(1,a+1)]
lst2=[]

for i in lst1:
    if i!=1:
        lst2.append(i)
lst2.append(1)
print(lst2)
