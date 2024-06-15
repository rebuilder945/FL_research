def maxsum(list):
      list.reverse()
      x=list[1]
      y=list[2]
      return int(x+y)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

