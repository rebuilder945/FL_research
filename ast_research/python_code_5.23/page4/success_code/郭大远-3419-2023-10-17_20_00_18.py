def calDegrees(nums):
        counts={}
        for i in nums:
               if i not in counts:
                counts[i]=1
               else:
                counts[i]+=1
        calDegrees=max(counts.values())
        return calDegrees
              
                   
        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

