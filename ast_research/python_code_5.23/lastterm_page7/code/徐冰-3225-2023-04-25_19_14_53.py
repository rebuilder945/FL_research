def work(a) :
dora={0:1}
    i=1
    while i<=a:
        dora[i]=dora[i-1]*i
        i=i+1
    return dora
	

a = int(input())
ans = work(a)
print(ans)

