def work(a) :
    dict={}
    for i in range(a+1):
        if i==0:
            dict[0]=1
        else:
            m=1
            for x in range(1,i+1):
                
                m*=x
            dict[i]=m
    return dict

	

a = int(input())
ans = work(a)
print(ans)

