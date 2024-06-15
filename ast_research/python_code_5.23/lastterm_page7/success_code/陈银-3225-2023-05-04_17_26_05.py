def work(a) :
    dic={}
    b = 1
    for x in range(a+1):
        dic[x]=jiecheng(x)
    return dic
def jiecheng(x):
    c = 1
    for i in range(1,x+1):
        c*=i
    return c
	

a = int(input())
ans = work(a)
print(ans)

