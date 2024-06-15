a=list(input().split(','))
n,m=eval(input(""))
if n <=(len(a)-1) and n >=(-len(a)):
    b=[a[n]]*m
    a.extend(b)
    a=[int(x) for x in a]
    print(a)
else:
    print("error")

       
