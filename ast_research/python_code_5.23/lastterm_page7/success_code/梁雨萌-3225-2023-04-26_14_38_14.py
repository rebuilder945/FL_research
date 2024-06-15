def work(a) :
    dic={}
    for i in range(0,a+1,1):
        num=1
        if i>0:
            for j in range(1,i+1,1):
                num=num*j
        dic[i]=num
    return(dic)
	

a = int(input())
ans = work(a)
print(ans)

