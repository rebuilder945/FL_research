lst1=list(input().split(","))
lst2=eval(input())
lst3=[]
n=len(lst1)
for x in range(n):
    a=[lst1[x]+","+lst2[x]]
    lst3.append(a)
print(lst3)


