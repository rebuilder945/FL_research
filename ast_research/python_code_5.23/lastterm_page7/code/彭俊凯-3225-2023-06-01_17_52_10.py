def work(a) :
a=list(range(a))
    print(a)
    b=[1]
    for i in a[1:]:
        c=1
        while i!=1:
            c=i*c
            i+=-1
        b.append(c)
    print(b)
    return dict(zip(a,b)
	

a = int(input())
ans = work(a)
print(ans)

