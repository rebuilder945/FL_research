a=str(input())
c=str(input())
b=[a]
for i in len(list(a)):
    n=b[-1].copy().pop(0)
    m=b[-1].copy()+n
    b.append(m)
if c in b:
    print('Ture')
else:
    print("False")
