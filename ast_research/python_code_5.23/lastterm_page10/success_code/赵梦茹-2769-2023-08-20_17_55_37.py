z=input()
print(z)
a=[chr(x) for x in range(ord('a'),ord('z')+1)]
b=[chr(y) for y in range(ord('A'),ord('Z')+1)]
for i in z:
    if i in a:
        s=a.index(i)
        i=a[25-s]
        print(i,end="")
    elif i in b:
        s=b.index(i)
        i=b[25-s]
        print(i,end="")
    else:
        print(i,end="")
