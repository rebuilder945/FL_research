def work(a) :
    b=1
    A={}
    for i in range[1:a+1]:
        b*=i
        A[i]=b
    return A
            
	

a = int(input())
ans = work(a)
print(ans)

