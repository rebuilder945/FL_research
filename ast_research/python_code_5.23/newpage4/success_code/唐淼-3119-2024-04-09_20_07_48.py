a=eval(input())
for i in a:
    b=a.count(i)
    if b!=1:
        a.remove(i)
print(a)
