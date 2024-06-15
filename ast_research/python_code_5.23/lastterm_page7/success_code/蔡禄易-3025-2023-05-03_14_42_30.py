a = input().split()
b = {}
ls1 = []
for i in a:
    b[i] = a.count(i)
for m in b:
    if m == max(b,key=b.get):
        ls1.append(m)
ls1.sort()
for x in ls1:
    print(x,end=" ")
    print(max(b.values))
