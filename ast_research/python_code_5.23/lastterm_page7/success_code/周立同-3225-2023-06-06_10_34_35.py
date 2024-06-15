def work(a) :
    lst=[x for x in range(0,a+1)]
    dic1={}
    for i in lst:
        if i==0 or i==1:
            dic1[i]=1
        else:
            a=i*lst[i-1]
            dic1[i]=a
            lst[i]=a
    return dic1
	

a = int(input())
ans = work(a)
print(ans)

