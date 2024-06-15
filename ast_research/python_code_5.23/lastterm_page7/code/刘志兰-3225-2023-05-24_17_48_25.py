def work(a) :
work={}
result=1
for i in range(x+1):
if i==0:
work[i]=1
else:
result*=i
work[i]=result
return work
	

a = int(input())
ans = work(a)
print(ans)

