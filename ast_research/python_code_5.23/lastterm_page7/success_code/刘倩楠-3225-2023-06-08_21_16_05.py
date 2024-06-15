def work(a) :
    num={}
    s=1
    for i in range(0,a+1):
        s*=i
        num[i]=s
        i+=1
    return num
	

a = int(input())
ans = work(a)
print(ans)

