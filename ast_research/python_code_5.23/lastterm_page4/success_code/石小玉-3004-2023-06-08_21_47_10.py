import math
def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i==0:
                return False
    return True
    
nums=eval(input())
nums2=[]
for x in nums:
    if sushu(x)==True:
        nums2.append(x)
    else:
        pass
print(nums2)

