def calDegrees(nums):
    list=[]
    for x in nums:
        n=nums.count(x)
        list.append(n)
    return(max(list))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

