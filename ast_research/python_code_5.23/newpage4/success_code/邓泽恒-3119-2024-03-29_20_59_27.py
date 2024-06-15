a=eval(input())
for x in a:
    b=a.count(x)
    for i in range(b-1):
        a.remove(x)
print(a)
