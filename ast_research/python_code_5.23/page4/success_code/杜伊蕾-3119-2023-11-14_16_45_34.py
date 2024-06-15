a=eval(input())
for x in reversed(a):
    if a.count(x)>1:
        for i in range((a.count(x))-1):
            a.remove(x)
print(a)
