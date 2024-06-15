def calDegrees(nums):
        for i in range(len(nums)):
             a=list(nums.count(i),end="")
             print(max(a))
        


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

