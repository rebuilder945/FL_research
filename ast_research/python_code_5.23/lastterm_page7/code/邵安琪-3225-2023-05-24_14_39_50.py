def work(a) :
 dic={}
    for i in range(0,a+1):
        b=1
        for x in range(1,i+1):
            b*=x
        dic.setdefault(i,b)
 return(dic)
	

a = int(input())
ans = work(a)
print(ans)

