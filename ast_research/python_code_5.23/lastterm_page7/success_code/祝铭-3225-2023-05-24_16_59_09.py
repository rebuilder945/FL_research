def work(a) :
    numls = []
    tmls = []
    b = 1
    for i in range(a+1) :
        numls.append(i)
        tmls.append(b)
        b *= (i+1)
    di = dict(zip(numls,tmls))
    return di
	

a = int(input())
ans = work(a)
print(ans)

