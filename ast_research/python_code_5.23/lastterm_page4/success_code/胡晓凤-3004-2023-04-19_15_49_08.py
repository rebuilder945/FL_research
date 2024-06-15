# import math
# def isPrime(num):
#     if num<0 or num in (0,1):
#      return False
#     for i in range(2,int(math.sqrt(num))+1):
#          if num%i==0:
#             return False
#     return True
# n=eval(input())
# if n%2==0 and 2<=n<22000000000:
#     for p in range(2,n):
#         if isPrime(p) and isPrime(n-p):
#             print("%s=%s+%s"%(n,p,n-p))
#             break
def sushu(num):
    y=True
    if num==1 or num==0:
        y=False
    for i in range(2,num):
        if num%i==0:
            y=False
    return y
ls1=eval(input())
ls2=[]
for i in range(len(ls1)):
    num=int(ls1[i])
    if sushu(num):
        ls2.append(ls1[i])
    else: pass
print(ls2)

