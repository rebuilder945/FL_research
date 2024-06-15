def maxsum(nums):
      t=[a+b for a in nums for b in nums]
    return max(t)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

