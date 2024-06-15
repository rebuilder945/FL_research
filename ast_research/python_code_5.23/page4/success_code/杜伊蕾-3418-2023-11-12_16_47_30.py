def maxsum(a):
    a.sort() 
    n = len(a) // 2
    result = sum(a[i] for i in range(0, n * 2, 2))
    return result
  




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

