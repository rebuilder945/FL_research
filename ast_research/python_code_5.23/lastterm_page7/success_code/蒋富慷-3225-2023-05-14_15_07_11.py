def work(a) :
    b = {}
    for i in range(a+1):
        if i <= 1:
            b[i] = 1
        else:
            c = 1
            for x in range(1,i+1):
                c = c*x
            b[i] = c
    return b
	

a = int(input())
ans = work(a)
print(ans)

