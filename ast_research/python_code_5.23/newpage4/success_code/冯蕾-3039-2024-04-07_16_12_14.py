lst=eval(input())
a=max(lst)
b=min(lst)
lst1=[]
for i in lst:
    if i!=a and a!=b:
        lst1.append(i)
print(lst1)

