def work(a) :
    dic={}
    bs=a
    bi=a
    i=1
    if a>=2:
        for x in range(a-1):
            while i<a:
                bs=bs*i
                i +=1
            dic[a]=bs
            a -= 1
            i=1
            bs=a
        dic[1]=1
        dic[0]=1
        return dic
    elif a==1:
        dic[1]=1
        dic[0]=1
        return dic
    else:
        dic[0]=1
        return dic
	

a = int(input())
ans = work(a)
print(ans)

