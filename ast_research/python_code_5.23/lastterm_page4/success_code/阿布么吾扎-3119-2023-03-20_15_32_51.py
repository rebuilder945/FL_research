a=eval(input())
b=a.copy()
for x in b:
    ge=a.count(x)
    if ge>=2:
        for i in range(ge-1):
            a.remove(x)
print(x)            
