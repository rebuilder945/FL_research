def work(a) :
    b=1
    dic={}

    if a>1:    
        dic[0]=1
        dic[1]=1
        for i in range(2,a+1):
            for c in range(1,i+1):
                b=c*b
            dic[i]=b
            b=1
        
    elif a==0:
        dic[0]=1
    elif a==1:
        dic[0]=1
        dic[1]=1
    return dic
	

a = int(input())
ans = work(a)
print(ans)

