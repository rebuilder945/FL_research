def calDegrees(nums):
       nums  =  eval(input())
       a=[]
       for i in eval(input())
            if i not in nums:
               a[i]=1
            else:
               a[i]+=1
       return max(a.values())
          
                
       


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

