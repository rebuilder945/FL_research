a = eval(input())
b = []
f = 1
for i in a:
    if a.count(i)==1 and i not in b:
        b.append(i)
        f = 0
if f:
    print(False)    
b.sort()
print(*b,sep=',')
