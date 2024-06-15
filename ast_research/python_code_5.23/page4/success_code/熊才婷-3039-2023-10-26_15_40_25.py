lst=eval(input())
x=min(lst)
y=max(lst)
for i in lst:
    if i==x or i==y:
        lst.remove(i)
print(lst)

