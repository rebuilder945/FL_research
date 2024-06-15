nums=list(input())
n,m=eval(input())
x=len(nums)
if abs(n)<x and n>=0:
    a=nums[n]
    b=nums.count(a)
    i=1
    while b>=i:
        nums.append(a)
        i=i+1
    print(nums)
elif abs(n)>=x and n<0:
    a=nums[n]
    b=nums.count(a)
    i=1
    while b>=i:
        nums.append(a)
        i=i+1
    print(nums)
else:
    print("error")


