def calDegrees(nums):
    a=[]
    for x in nums:
        a.append(nums.count(x))
        return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

