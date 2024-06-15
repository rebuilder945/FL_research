def calDegrees(nums):
    k=[]
    for c in nums:
        b=nums.count(c)
        k.append(b)
    d=max(k)
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

