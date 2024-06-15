a = eval(input())
b = []
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
b.sort()
c=str(b)
if b ==[]:
    print("False")
else:
    print(c[1:-1])
