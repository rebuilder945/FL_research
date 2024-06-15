def work(a) :
    dic1={}
    for i in range(a+1):
        if i==0:
            dic1[i]==1
        else:
            for n in range(1,i+1):
                n=1*n
            dic1[i]==n
    return dic1
	

a = int(input())
ans = work(a)
print(ans)

