def work(a) :
dic={}
i=0
x=1
dic[i]=x
for i in range(1,a+1):
    x*=i
    dic[i]=x               
return dic
	

a = int(input())
ans = work(a)
print(ans)

