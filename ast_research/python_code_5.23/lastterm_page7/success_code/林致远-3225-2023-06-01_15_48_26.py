def work(a) :
    num = {}
    for x in range(a+1):
        num[x]=factorial(x)
    return num

def factorial(num):
    a=1
    for i in range(1,num+1):
         a*=i
    return a
	

a = int(input())
ans = work(a)
print(ans)

