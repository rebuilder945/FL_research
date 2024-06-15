def work(a) :
def jiecheng(y):
    c=1
    for x in range(y+1):
        c*=x
    return c
dic={}
for i in range(a+1):
    b=jiecheng(i)
    dic[i]=b
	

a = int(input())
ans = work(a)
print(ans)

