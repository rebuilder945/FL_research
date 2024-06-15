def calDegrees(nums):
    max = 0
    length = len(nums)
    for i in range(0,length):
        count = 1
        for j in range(0,length):
            if(nums[i]==nums[j]):
                count += 1
     max = count
     return max



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

