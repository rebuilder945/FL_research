def work(a) :
    jc={}
    item=range(a+1)
    jc[0]=1
    def main(num):
        a=1
        for i in range(1,num+1):
            a*=i
        return a
    for i in range(1,a+1):
        jc[i]=main(i)
    return jc
	

a = int(input())
ans = work(a)
print(ans)

