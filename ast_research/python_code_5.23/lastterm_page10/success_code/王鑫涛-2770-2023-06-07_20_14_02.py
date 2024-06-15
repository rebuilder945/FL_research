a=str(input())
c=str(input())
b=[a]
for i in range(len(list(a))):
    b.append(b[-1])
    n=b[-1].pop(0)
    m=b[-1]+n
    b.append(m)
if c in b:
    print('Ture')
else:
    print("False")
