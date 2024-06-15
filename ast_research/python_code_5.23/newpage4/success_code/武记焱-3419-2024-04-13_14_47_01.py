def calDegrees(nums):
    list1=[]
    for i in nums:
        x=nums.count(i)
        list1.append(x)
    y=max(list1)
    return(y)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

