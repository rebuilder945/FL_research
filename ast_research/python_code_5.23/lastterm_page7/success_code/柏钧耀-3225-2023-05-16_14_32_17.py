def work(a) :
    dic={}
    dic[0]=1
    for i in range(1,int(a)+1):
        c=1
        for j in range(1,i+1):
            c*=j
            dic[i]=c
    return dic
        
	

a = int(input())
ans = work(a)
print(ans)

