def work(a) :
    dic={}
    dic[0]=1
    for i in range(1,a+1):
        m=1
        fi=1
        while m<=i:
            fi *=m
            m+=1
        dic[i]=fi
    return dic
	

a = int(input())
ans = work(a)
print(ans)

