def work(a) :
    b=0
    c=1
    dic={0:1}
    if a==0:
        return dic
    else:
        while b<a:
            b+=1
            c=c*b
            dic[b]=c
        return dic
	

a = int(input())
ans = work(a)
print(ans)

