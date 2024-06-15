def work(a) :
def jiecheng(i):
    c=1
    for x in range(i+1):
        c*=x
    return c
dic={}
for i in range(a+1):
    b=jiecheng(i)
    dic[i]=b
	

a = int(input())
ans = work(a)
print(ans)

