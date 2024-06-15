
def calDegrees(nums):
    z = 0
    for i in nums:
        if nums.count(i)>z:
            b = nums.count(i)
        return(b)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

