def work(a) :
    a= {0: 1}
    b = 1
    for i in range(1, a+1):
        b *= i
        ans[i] = b
    return a
	

a = int(input())
ans = work(a)
print(ans)

