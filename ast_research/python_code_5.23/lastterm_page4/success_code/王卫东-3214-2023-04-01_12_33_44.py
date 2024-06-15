a = eval(input())
b = []
for x in a:
    if x ==0:
        a.remove(x)
        b.append(x)
print(a+b)        
