def work(a) :
    def jiecheng(x):
    i=0
    b=1
        if x==0:
            return 1
        else:
            while i<x:
        c=b
        d=c*b
        b=b+1
        d=d*b
        i=i+1
        return d
           
    dic={}
    for x in range(a+1):
        dic[x]=jiecheng(x)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

