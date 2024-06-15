def calDegrees(nums):
    ls=[]
    for i in nums:
        ls.append(nums.count(i))
        return max(ls)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

