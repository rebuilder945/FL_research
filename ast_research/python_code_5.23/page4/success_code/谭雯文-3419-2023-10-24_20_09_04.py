def calDegrees(nums):
    ls1=[]
    for i in range(len(nums)):
        a=nums.count(nums[i])
        ls1.append(a)
    b=max(ls1)
    return(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

