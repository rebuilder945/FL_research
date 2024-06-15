import math
def isPrime(num):#定义素数函数
    if num<0 or num in (0,1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return num
N=eval(input())
for x in range(2,N+1):#循环遍历2到N的全部值
    if isPrime(x) and isPrime(N-x) and x<=N-x:#判断分解数是否是素数
        p=x
        q=N-x
        print("%d = %d + %d"%(N,p,q))
        break
