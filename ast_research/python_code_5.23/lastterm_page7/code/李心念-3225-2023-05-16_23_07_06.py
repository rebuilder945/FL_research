def work(a) :
dic = {}
for x in range(a):
    if x == 0:
        dic[0]=0
    else:
        a = 1
        for y in range(1,x+1):
            a = a*x
        dic[x]=a
return dic
	

a = int(input())
ans = work(a)
print(ans)

