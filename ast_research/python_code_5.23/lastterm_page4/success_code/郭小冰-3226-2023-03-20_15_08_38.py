def majorityElement(nums):
       count,candi=0,0
       for i in nums:
             if i ==candi:
                 count+=1
             else:
                 if count==0:
                      candi=i
                      count=1
                 else:
                      count-=1
       return candi
                    





nums = eval(input())
y = search(nums)
print(y)


