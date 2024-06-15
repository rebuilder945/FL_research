def calDegrees(nums):
    ls=[]
    for x in nums:
        c=nums.count(x)
        ls.insert(1,c)
        d=max(ls)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

