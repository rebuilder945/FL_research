def work(a) :
    b=a
    if a==0:
        return 1
    else:
        while a>1:
            b*=(a-1)
            a-=1
        return b
	

a = int(input())
ans = work(a)
print(ans)

