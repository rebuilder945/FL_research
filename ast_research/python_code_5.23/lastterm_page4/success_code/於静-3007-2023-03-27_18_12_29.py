nums=eval(input())
n,m=eval(input())
length=len(nums)
if n>m or n<0 or m>length:
    print("error")
else:
    l1=nums[:n]
    l2=nums[m:]
    l3=l1+l2
    print(l3)
