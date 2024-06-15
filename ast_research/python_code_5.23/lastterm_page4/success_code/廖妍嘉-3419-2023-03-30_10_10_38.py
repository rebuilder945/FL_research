def calDegrees(nums):
    for i in nums:
        ls=[]
        b=nums.count(i)
        ls.append(b)
    return max(ls)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

