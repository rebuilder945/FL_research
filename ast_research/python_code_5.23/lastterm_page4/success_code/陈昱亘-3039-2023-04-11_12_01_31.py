lst1=eval (input())
n=max(lst1)
m=min(lst1)
lst2=[]
for i in lst1:
    if i not in [n,m]:
        lst2.append(i)
print(lst2)
