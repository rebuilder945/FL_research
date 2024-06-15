l=eval(input())
for i in l:
    b=l.count(i)
    while b>=2:
        l.remove(i)
        b-=1
print(l)
