def work(a) :
    c = {}
    for x in range(a+1):
        b = 1
        for y in range(1,x+1):
            b = b*y
        c[x] = b
    return(c)
	

a = int(input())
ans = work(a)
print(ans)

