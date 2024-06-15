def maxsum(nums):
      ls = []
      l = len(nums)/2
      for i in range(l):
            m = max(nums)
            nums.remove(m)
            ls.append(max(nums))
            nums.remove(max(nums))
      s = sum(ls)
      return s
            




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

