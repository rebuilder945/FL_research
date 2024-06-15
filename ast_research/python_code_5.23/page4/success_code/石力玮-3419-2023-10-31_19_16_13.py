def calDegrees(nums):
    counter=Count(nums)
    maxcounter=max(counter.value())
    return  maxcounter


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

