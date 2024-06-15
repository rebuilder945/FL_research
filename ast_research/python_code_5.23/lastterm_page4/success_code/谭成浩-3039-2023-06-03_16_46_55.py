lst=eval(input())
m=max(lst)
x=min(lst)
lst1=[]
for i in lst:
    if i==m or i ==x:
        continue
    else:
        lst1.append(i)
print(lst1)
