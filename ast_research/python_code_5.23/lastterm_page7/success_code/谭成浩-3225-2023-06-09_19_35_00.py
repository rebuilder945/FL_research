def work(a) :
    dic={} 
    for i in range(a+1):
        dic[i]=jie(i)
    return dic
def jie(n):
    x=1
    for i in range(n):
        x=x*(i+1)
    return x

	

a = int(input())
ans = work(a)
print(ans)

