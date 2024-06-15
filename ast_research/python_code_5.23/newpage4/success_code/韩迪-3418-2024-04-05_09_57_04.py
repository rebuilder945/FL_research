def maxsum(nums):
       a=min(nums)
       nums.remove(a)
       b=min(nums)
       return(a+b)
       




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

