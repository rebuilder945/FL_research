def work(a) :
    b = {}
    for i in range(a+1):
        if i <= 0:
            b[i] = 0
        else:
            c = 1
            for x in range(1,i+1):
                c = c*x
            b[i] = c
    return b
	

a = int(input())
ans = work(a)
print(ans)

