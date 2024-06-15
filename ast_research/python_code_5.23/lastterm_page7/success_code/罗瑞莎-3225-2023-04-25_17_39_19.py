def work(a) :
    dic={}
    num=1
    if a==0:
        dic[int("0")]=1
        return dic
    elif a>0:
        for i in range(0,a+1):
            dic[i]=1         
        return dic
	

a = int(input())
ans = work(a)
print(ans)

