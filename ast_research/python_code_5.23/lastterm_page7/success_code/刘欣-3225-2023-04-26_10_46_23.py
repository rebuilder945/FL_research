def work(a) :

    key1=[]
    value1=[]
    for i in range(a+1):
        key1.append(i)
        value1.append(factorial(i))
        dic=dict(zip(key1,value1))
    return dic
def factorial(n):
    if n==1:
        return 1
    r=n*factorial(n-1)
    return r
	

a = int(input())
ans = work(a)
print(ans)

