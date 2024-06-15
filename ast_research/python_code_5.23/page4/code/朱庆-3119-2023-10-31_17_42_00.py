a = eval(input())
a.reserve()
b = []
for x in a:
    if x not in b:
    b.append(x)
    #b.append(a.pop(a.index(x)))
b.reserve()
print(b)    

