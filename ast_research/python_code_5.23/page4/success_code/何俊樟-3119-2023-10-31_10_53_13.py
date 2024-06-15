a=eval(input())
for x in a:
    if a.count(x)>1:
        b=a.count(x)
        for y in range(b-1):
            a.remove(x)
    else:
        pass
print(a)
    

