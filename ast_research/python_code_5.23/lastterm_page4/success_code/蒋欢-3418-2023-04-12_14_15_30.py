import random
def minsum(nums):
    n=int(len(nums)/2)
    mins=[]
    for x in range(n):
        nums2=nums[2*x:2*x+2]
        mins.append(min(nums2))
    return sum(mins)
def maxsum(nums):
    n=int(len(nums)/2)
    m=1
    for p in range(1,n+1):
        m=m*p
    sums=[]
    for i in range(m+100):
        random.shuffle(nums)
        sums.append(minsum(nums))
    return max(sums)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

