def work(a) :
    if a<0:
        return
    x=1
    else:
        for i in range(a):
            x*=i+1
            dic[i+1]=x
    return dic
	

a = int(input())
ans = work(a)
print(ans)

