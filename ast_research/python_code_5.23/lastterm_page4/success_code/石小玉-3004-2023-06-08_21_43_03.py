import math
def sushu(n):
    for i in range(2,int(math.sqrt(n))+1) and i>=2:
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

