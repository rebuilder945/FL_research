def calDegrees(nums):
    lst=[]
    for i in nums:
        d=nums.count(i)
        lst.append(d)
    a=max(lst)
    return a


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

