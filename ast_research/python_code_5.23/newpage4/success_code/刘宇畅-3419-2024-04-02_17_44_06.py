def calDegrees(nums):
    d=[]
    for i in (nums):
        a=nums.count(i)
        d.append(a)
    return max(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

