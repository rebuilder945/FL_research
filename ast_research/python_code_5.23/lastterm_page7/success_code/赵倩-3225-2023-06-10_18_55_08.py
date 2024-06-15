def work(a) :
    d={0:1}
    b=1
    if x!=0:
        for i in range(1,x+1):
            b*=i
            d[i]=b
        return d
    if x==0:
        return d
 
	

a = int(input())
ans = work(a)
print(ans)

