def work(a) :
s = {}
    for i in range(a):
        if i == 0:
            s['0'] = 1
        elif i > 0:
            for j in range(1,i+1):
                b *= j
            s['i'] = b   
    return s
	

a = int(input())
ans = work(a)
print(ans)

