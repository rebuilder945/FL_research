def calDegrees(nums):
    list1 = []
    for x in nums:
        list1.append(nums.count(x))
    a = max(list1)       
    return(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

