def work(a) :
    c=[]
    for b in range(1,a+1):
        for i in range(b,a+1):
            b*=i
c.append(b)

	

a = int(input())
ans = work(a)
print(ans)

