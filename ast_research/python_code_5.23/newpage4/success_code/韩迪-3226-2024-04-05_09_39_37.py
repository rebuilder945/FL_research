def search(nums):
       n=len(nums)
       s=[]
       for i in nums:
             if nums.count(i)>n//2:
                    s.append(i)
             else:
                    pass
       if s==[]:
             return("False")
       else:
             return(i)





nums = eval(input())
y = search(nums)
print(y)


