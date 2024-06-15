def calDegrees(nums):
    list1=[]
    for x in nums:
        a=nums.count(x)
        list1.append(a)
    return max(list1)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

