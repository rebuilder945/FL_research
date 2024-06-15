def work(a) :
    def jiecheng(x):
        i=0
        b=1
        c=1
        if x==0:
            return 1
        else:
            while i<x:
                d=b*c
                c=c+1
                b=d
                i=i+1
            retrun d
 
    dic={}
    for x in range(a+1):
        dic[x]=jiecheng(x)
    return dic
	

a = int(input())
ans = work(a)
print(ans)

