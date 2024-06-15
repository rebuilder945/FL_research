def calDegrees(nums):
    lst = [ nums.count(x) for x in nums]
    return max(lst)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

