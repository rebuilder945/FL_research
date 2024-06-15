def calDegrees(nums):
       lst={}
       for x in nums:
            if x not in nums:
                lst[x]=1
            else:
                lst[x]+=1
       return max(lst.values())
            
       


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

