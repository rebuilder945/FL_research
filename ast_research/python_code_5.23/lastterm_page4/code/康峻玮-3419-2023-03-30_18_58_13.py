def calDegrees(nums):
    length = len(nums)
    for i in range(0,length+1):
        c = 1
    for j in range(i+1,length+1):
        if(nums[i]==nums[j]):
        c + = 1
     return c

        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

