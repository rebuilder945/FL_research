def calDegrees(l):
      n=[l.conut(x) for x in set(l)]
      return max(n)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

