def work(a) :
    dic={}
    for i in range(a+1):
        j=1
        if i==0:
            dic[i]=j
        else:
            for x in range(1,i+1):
                j*=x
            dic[i]=j
    return dic
	

a = int(input())
ans = work(a)
print(ans)

