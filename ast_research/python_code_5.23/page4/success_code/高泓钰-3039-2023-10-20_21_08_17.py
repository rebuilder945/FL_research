lst=eval(input())
m=max(lst)
n=min(lst)
for i in lst:
    if m in lst:
         lst.remove(m)
for x in lst:
    if n in lst:
        lst.remove(n)
print(lst)

