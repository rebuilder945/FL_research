'''a=eval(input())
for x in reversed(a):
    if a.count(x)>1:
        for i in range((a.count(x))-1):
            a.remove(x)
print(a)'''


a=eval(input())
for x in reversed(a):
    b=a.count(x)
    if b>1:
        for i in range(b-1):
            a.remove(x)
print(a)


