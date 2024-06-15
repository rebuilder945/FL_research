def calDegrees(nums) :
     for i in nums:
        a = max(i.count())
        return a



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

