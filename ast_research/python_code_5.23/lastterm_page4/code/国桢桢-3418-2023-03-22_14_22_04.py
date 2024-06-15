def maxsum(nums):
 v = sum(sorted(nums)[::2])
return("%.d"%(v))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

