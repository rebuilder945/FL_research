def work(a) :
    d={0:1}
    b=1
    if a!=0:
        for i in range(1,a+1):
            b*=i
            d[i]=b
        return d
    if a==0:
        return d
 
	

a = int(input())
ans = work(a)
print(ans)

