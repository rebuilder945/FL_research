nums=eval(input())
n,m=eval(input())
length=len(nums) 
if n>m or n<0 or m>length:
    print("error")
else:
    del nums[n:m]    
    print(nums)

