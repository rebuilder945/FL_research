def work(a) :
    dic=dict()
    
    if a == 0:
        sum=1
        dic.setdefault('0','1')
    elif a>0:    
        sum=1
        for i in range(1,a + 1):
            sum*=i
            dic.setdefault(i,sum)
    return dic
    
	

a = int(input())
ans = work(a)
print(ans)

