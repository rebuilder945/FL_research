def maxsum(nums):
      n = int(len(nums)/2)
      list_d3=[]
      for i in range(n+1):
              list_part1=nums[i:i+1]
              d1 = min(list_part1)
              nums_copy=nums[:]
              del nums_copy[i:i+1]
              list_part2 = nums_copy
              d2 = min(list_part2)
              d3 = d1+d2
               list_d3.append(d3)
               list_d3 = list_d3[:]
      d4 = max(list_d3)
      return d4
     




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

