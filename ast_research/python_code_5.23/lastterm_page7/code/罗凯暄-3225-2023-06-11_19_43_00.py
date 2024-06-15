def work(a) :
    dic=dict()
    for i in range(0,a+1):
        b=i
        c=1
        for x in range(1,b+1):
            c*=x
        dic[b]=c
return dic
	

a = int(input())
ans = work(a)
print(ans)

