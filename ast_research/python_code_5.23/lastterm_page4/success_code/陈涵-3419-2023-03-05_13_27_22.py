def calDegrees(nums):
       for x in nums:
            cnt=nums.count(x)
       return max(cnt)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

