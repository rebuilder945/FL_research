def work(a) :

    dic={}
    for x in range(a):
        dic[x]=jiecheng(x)
def jiecheng(m):
    n = 1
    for i in range(1,m+1):
        n*=i
    return n
    
	

a = int(input())
ans = work(a)
print(ans)

