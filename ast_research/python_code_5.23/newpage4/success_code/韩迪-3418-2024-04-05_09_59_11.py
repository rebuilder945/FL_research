def maxsum(nums):
       nums.sort()
       a=nums[-2]
       b=nums[-4]
       return(a+b)
       




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

