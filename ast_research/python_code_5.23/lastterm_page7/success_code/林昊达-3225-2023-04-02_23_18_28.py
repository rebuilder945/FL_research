def work(a) :
    dic={}
    for i in range(0,a+1):
        add=1
        for j in range(i,0,-1):
            add=add*j
        dic[i]=add
    return dic
	

a = int(input())
ans = work(a)
print(ans)

