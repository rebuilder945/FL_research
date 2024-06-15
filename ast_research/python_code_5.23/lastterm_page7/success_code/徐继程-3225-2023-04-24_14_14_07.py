def work(a) :
    dic={}
    for i in range(a+1):
        dic.update({i:jiecheng(i)})
    return dic

def jiecheng(i):
    a=1
    for x in range(i):
        a*=x+1
    return a
	

a = int(input())
ans = work(a)
print(ans)

