def calDegress(nums):
    n1=[]
    for x in nums:
       n1.append(nums.count(x))
    return max(n1)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

