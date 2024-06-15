def work(a) :
  dict={}
  for i in range(0,a+1):
    if i==0:
        dict[i]=1
    else:
        m=1
        m*=i
        dict[i]=m
	

a = int(input())
ans = work(a)
print(ans)

