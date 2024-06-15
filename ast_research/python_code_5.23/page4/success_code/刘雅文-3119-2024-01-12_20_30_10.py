a=eval(input())
for x in reversed(a):
    b=a.count(x)
    if b>1:
        for i in range(b-1):
            a.remove(x)
print(a)
