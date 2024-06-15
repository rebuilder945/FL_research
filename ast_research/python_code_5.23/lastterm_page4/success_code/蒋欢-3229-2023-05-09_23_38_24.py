def Find(n):
    m=[x for x in n if n.count(x)==1]
    m.sort()
    if m==[]:
        print("False")
    else:
            a=[str(i) for i in m]
            b=",".join(a)
            print(b)
n=eval(input())
Find(n)
