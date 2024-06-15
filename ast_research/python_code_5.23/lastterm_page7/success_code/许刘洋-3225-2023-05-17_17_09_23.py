def work(a) :
    dic={}
    for i in range(a+1):
        dic[i]=jc(i)
    return dic
def jc(n):
    r=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            r*=i
        return r
	

a = int(input())
ans = work(a)
print(ans)

