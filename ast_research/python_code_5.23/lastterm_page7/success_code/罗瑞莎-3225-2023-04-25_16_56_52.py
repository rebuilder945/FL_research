def work(a) :
    dic={}
    num=1
    if a==0:
        dic["0"]=1
        return dic
    elif a>0:
        for i in range(0,a+1):
            for j in range(1,i+1):
                num*=i
                dic["i"]=num
        return dic
	

a = int(input())
ans = work(a)
print(ans)

