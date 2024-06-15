def work(a) :
    
    ls=[]
    b=1
    i=0
    dic={}
    while True:
        if  n==0:
            ls.append(1)
            break
        else:
            i+=1
            n-=1
            b=b*i
            ls.append(b)
    ls.sort()
    for x in range(i+1):
        dic[x]=ls[x]
    return dic
	

a = int(input())
ans = work(a)
print(ans)

