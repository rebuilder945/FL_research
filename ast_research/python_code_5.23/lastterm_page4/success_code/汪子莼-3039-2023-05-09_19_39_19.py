a=eval(input())
b=max(a)
c=min(a)
lst=a.copy()
for i in a:
    if i==b or i ==c:
        lst.remove(i)
print(lst)
