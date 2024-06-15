def maxsum(nums):
      nums.sort()
      nums.reverse()
      min=[]
      lst=[]
      for i in range(0,len(nums),2):
           a=nums[i]
           b=nums[i+1]
           lst.append(a)
           lst.append(b)
           c=min(lst)
           min.append(c)
      return sum(min)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

