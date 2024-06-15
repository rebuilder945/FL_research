l=eval(input())
l2=l.copy()
for i in l:
    a=l2.count(i)
    if a>1:
        l2.remove(i)
        a-=1
print(l2)

