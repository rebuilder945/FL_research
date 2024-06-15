def work(a) :
d={}
d[0]=1
for i in range(1,a+1):
    y=1
    for x in range(1,i+1):
        y*=x
    d[i]=y
return d
	

a = int(input())
ans = work(a)
print(ans)

