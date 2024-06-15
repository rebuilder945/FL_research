lis1 =eval(input())
a =max(lis1)
b =min(lis1)
c =lis1.count(a)
d =lis1.count(b)
if a==b:
    print([])
else:
    for i in range(c):
        lis1.remove(a)
    for x in range(d):
        lis1.remove(b)
    print(lis1)
