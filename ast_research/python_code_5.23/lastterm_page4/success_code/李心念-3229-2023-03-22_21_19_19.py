a = eval(input())
b = []
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
b.sort()
if b ==[]:
    print("False")
else:
    c=''
    for i in range(len(b)):
        c=c+str(b[i])+','
    print(c[0:-1])
