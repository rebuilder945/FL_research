a=eval(input())
a1=a.copy()
for i in a:
    if a.count(i)>=2:
        a1.remove(i)
if len(a1)>=1:
    a1.sort()
    print(a1)
else:
    print(False)
