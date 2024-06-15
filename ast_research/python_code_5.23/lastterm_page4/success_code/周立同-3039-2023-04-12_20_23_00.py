lst=eval(input())
lst1=[]
a=min(lst)
b=max(lst)
for i in lst:
    if i!=a and i!=b:
        lst1.append(i)
    else:
        continue
print(lst1)
