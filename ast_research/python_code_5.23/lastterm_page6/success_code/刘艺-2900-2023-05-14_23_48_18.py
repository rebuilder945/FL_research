def isPrime(num):
    jishu=0
    for i in range(2,num):
        if num%i==0:
            jishu=1
    if jishu==0 and num!=1:
        return True
    else:
        return False
def reverseNumber(num):
    b=str(num)
    c=list(b)
    c.reverse()
    jishu=0
    for i in c:
        jishu=jishu*10+int(i)
    return jishu 


N = int(input())
for n in range(1,N+1):
    if isPrime(n) and reverseNumber(n) == n:
        print(n) 


