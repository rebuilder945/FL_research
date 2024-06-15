def maxsum(nums):
      nums.sort(reverse=true)
      m=[]
      lst=[]
      for i in range(0,len(nums),2):
           a=nums[i]
           b=nums[i+1]
           lst.append(a)
           lst.append(b)
           c=min(lst)
           m.append(c)
      return sum(m)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

