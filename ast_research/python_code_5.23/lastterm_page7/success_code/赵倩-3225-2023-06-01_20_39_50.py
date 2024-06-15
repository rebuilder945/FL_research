def work(a) :
    d={0:1,1:1}
    b=1
    c=2
    if a==0:
         return{0:1}
    elif a==1:
         return{0:1,1:1}
    else:
        for i in range(2,a+1):
            for y in range(i):
                    c=b*c
                    b+=1
                    d[b]=c
	

a = int(input())
ans = work(a)
print(ans)

