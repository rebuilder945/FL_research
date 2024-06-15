def work(a) :
dic={}
n=1
dic[0]=1
for x in range(1,a+1):
        n*=x
        dic[x]=n
return dic
	

a = int(input())
ans = work(a)
print(ans)

