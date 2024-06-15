def work(a) :
    dic={}
    dic[0]=1
    s=1
    for i in range(1,a+1):
        s=s*i
        dic[i]=s
    return dic

	

a = int(input())
ans = work(a)
print(ans)

