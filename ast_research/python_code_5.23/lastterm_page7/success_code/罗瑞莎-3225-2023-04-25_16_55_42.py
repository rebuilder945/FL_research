def work(a) :
    dic={}
    if x==0:
        dic["0"]=1
        return dic
    elif x>0:
        for i in range(0,x+1):
            for j in range(1,i+1):
                num*=i
                dic["i"]=num
        return dic
	

a = int(input())
ans = work(a)
print(ans)

