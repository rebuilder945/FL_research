def calDegrees(n):
      m=[n.count(x) for x in set(n)]
      return max(m)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

