def work(a) :
    if a==0:
        return 1
    else:
        return a*work(a-1)
	

a = int(input())
ans = work(a)
print(ans)

