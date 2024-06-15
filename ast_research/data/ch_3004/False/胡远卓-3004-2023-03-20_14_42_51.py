import math
def isprime(x):
    if x==1:
        return 0
    for i in range(2,int(math.sqrt(x))):
        if x%i==0:
            return 0
    return 1

nums=eval(input())
L=len(nums)
lst=[]
for i in range(L):
    if isprime(nums[i]):
        lst.append(nums[i])
print(nums)
