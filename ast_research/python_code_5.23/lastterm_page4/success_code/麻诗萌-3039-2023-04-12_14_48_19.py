lst=eval(input())
n=min(lst)
m=max(lst)
for i in lst :
    if i==m:
        lst.remove(m)
    elif i==n :
        lst.remove(n)
    else:
        lst=lst
print(lst)
