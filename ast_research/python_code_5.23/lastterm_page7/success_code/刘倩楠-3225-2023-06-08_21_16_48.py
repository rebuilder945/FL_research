def work(a) :
    num={0:1}
    s=1
    for i in range(1,a+1):
        s*=i
        num[i]=s
        i+=1
    return num
	

a = int(input())
ans = work(a)
print(ans)

