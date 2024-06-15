def work(a) :
    dic=dict()
    sum=1
    for i in range(0,a + 1):
        if i==0:
            sum=1
        elif i>0:
            sum*=i
        dic.setdefault(i,sum)
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

