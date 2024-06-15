def work(a) :
diction={}
    for i in range(a+1):
        if i==0:
            diction[i]==1
        else:
            for n in range(1,i+1):
                n=1*n
            diction[i]==n
	

a = int(input())
ans = work(a)
print(ans)

