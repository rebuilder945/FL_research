import math
def sushu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i==0:
            return False
    return True
    
nums=eval(input())
for x in nums:
    if sushu(x)==True:
        nums.remove(x)
    else:
        pass

print(nums)

