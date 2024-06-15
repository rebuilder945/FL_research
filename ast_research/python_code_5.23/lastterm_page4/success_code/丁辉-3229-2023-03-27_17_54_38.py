a=eval(input())
b=[a.count(i) for i in a]
for n in b:
    if n==1:
        m=b.index(n)
        p=a.pop(m)
        print("",p)
        continue
else:
    print("False")
