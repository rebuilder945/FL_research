lst=eval(input())
n=min(lst)
m=max(lst)
for i in lst :
    if i==m:
        lst.remove(m)
    else i==n:
        lst.remove(n)
print(lst)
