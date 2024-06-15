calDegrees = {}
for i in eval(input()):
      if i not in calDegrees:
          calDegrees[i] = 1
      else:
          calDegrees+=1


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

