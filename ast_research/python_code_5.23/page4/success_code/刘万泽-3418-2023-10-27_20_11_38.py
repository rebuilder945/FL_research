def maxsum(nums):
      a=nums.sort()
      t=min(a)
      b=[]
      for i in a:
           if i!=t:
               b.append(i)
           else:
                continue
      q=min(b)
      h=t+q            
      return h




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

