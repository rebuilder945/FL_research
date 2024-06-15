def work(a) :
    def f(n):
        result=1
        for i in range (1,n+1):
            result*=i
        return result
    dic={}
    for i in range(0,a+1):
        dic[i]=f(i)
    return dic    def f(n):
        result=1
        for i in range (1,n+1):
            result*=i
        return result
    dic={}
    for i in range(0,a+1):
        dic[i]=f(i)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

