def work(a) :
     dic={}
    if a==0:
        dic[0]=1
    else:
        dic[0]=1
        for i in range(a):
            k=i+1
            n=1
            for x in range(k):
                n*=(x+1)
            dic[k]=n
	

a = int(input())
ans = work(a)
print(ans)

