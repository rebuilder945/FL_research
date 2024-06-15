def work(a) :
    i=1
    dic={0:1}
    while i<=a:
        x=1
        for c in range(1,i+1):
            x*=c
            c+=1
        dic[i]=x
        i+=1
    return dic
	

a = int(input())
ans = work(a)
print(ans)

