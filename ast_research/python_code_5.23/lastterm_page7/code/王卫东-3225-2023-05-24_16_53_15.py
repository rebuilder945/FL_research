def work(a) :
dic={}
for x in range(1,a+1):
    c=1
    for y in range(1,x+1):
          c=c*y
     dic[x]=c
return dic
	

a = int(input())
ans = work(a)
print(ans)

