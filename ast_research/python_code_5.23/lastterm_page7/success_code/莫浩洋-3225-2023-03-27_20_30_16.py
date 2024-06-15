def work(a) :
 d = {}
 for i in range(0,a+1):
     num=1
     for x in range(1,i+1):
         num=num*x
     d[i]=num
 return d
	

a = int(input())
ans = work(a)
print(ans)

