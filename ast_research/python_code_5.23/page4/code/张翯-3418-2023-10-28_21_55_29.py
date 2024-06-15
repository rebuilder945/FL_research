def maxsum(nums):
      nums.sort()
      nums.reverse()
      min=[]
      for i in range(0,len(nums),2):
           a=[nums[i],nums[i+1])]
           b=min(a)
           min.append(b)
      return sum(min)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

