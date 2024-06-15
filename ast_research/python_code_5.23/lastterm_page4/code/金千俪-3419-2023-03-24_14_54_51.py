del calDegrees(nums) :
    for i in range(nums):
        nums.count(i)
        nums.max(i)
        return(nums)

        
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

