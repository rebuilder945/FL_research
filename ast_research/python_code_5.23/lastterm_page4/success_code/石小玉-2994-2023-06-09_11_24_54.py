nums=list(eval(input()))
n,m=eval(input())
h=int(n)
g=int(m)
x=len(nums)
if abs(h)<x and h>=0:
    a=nums[h]
    i=1
    while g>=i:
        nums.append(a)
        i=i+1
    print(nums)
elif abs(h)<=x and h<0:
    a=nums[h]
    i=1
    while g>=i:
        nums.append(a)
        i=i+1
    print(nums)
else:
    print("error")


