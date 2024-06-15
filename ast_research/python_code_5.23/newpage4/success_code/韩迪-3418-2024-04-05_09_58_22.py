def maxsum(nums):
       nums.sort()
       a=nums[1]
       b=nums[3]
       return(a+b)
       




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

