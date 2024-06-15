def work(a) :
    dic={0:1}    
    n=1
    for i in range(1,a+1):
        n=n*i
        dic[i]=n
    return dic
        
	

a = int(input())
ans = work(a)
print(ans)

