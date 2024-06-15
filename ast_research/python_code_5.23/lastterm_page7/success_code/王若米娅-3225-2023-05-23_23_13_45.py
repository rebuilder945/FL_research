def work(a) :
    dic={}
    for x in range(a+1):
        dic[x]=jiecheng(x)
    return dic
def jiecheng(x):
    if x==0:
        return 1
    else:
        return x*jiecheng(x-1)
	

a = int(input())
ans = work(a)
print(ans)

