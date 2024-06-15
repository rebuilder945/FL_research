def cou(nums):
    for x in nums:
        e = nums.count(x)
    return e
def calDegrees(nums):
    nums.sort(key=cou(nums))
    nums.reverse()
    f = nums.count([0])
    return f
nums = eval(input())
d = calDegrees(nums) 
print(d)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

