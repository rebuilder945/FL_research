def calDegrees(nums):
    a=[]
    for i in nums:
        a.append(nums.count(i))
    return max(a)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

