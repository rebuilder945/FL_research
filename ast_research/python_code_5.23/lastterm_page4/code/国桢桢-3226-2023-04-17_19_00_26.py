del search(nums):
 b=[]
 c=[]
 for i in nums:
     if i not in b:
           b.append(i)
 for x in b:
     e=nums.count(b)
     c.append(e)
 return max(c) 
      
      
 





nums = eval(input())
y = search(nums)
print(y)


