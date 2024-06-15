def work(a) :
    i=0
    b=1
    sum={}
    sum[i]=b
    i=i+1
    while i <=a:
        b=b*i
        sum[i]=b
        i=i+1
    return sum
	

a = int(input())
ans = work(a)
print(ans)

