nums=eval(input())
n,m=eval(input())
lengh=len(nums)
if n>m or n<0 or m>lengh:
    print("error")
else:
    l1=nums[:n]
    l2=nums[m:]
    l3=l1+l2
    print(l3)

