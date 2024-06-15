def work(a) :
    dic={}
    for i in range(a+1):
        i=b
        for x in range(1,i):
            i*=x
        dic['str(b)']=i
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

