def maxsum(nums):
      ls = []
      for i in range(len(nums)/2)
            m = max(nums)
            nums.remove(m)
            ls.append(max(nums))
            nums.remove(max(nums))
      s = sum(ls)
      return s
            




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

