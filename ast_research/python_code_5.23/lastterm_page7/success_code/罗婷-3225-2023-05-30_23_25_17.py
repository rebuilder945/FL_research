def work(a) :
    dict={}
    for i in range(a+1):
        if 1 == 0:
            dict[i]=1
        dict[i]=dict[i-1]*i
    return dict
	

a = int(input())
ans = work(a)
print(ans)

