def maxsum(sums):
    sums.sort()
    a=sums[0]+sums[1]
    print(a)
maxsum(eval(input()))
  





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

