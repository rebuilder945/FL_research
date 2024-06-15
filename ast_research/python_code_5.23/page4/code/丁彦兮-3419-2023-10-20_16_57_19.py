Def calDegrees:
       list={}
       for x in nums:
            if x not in nums:
                list[x]=1
            else:
                list[x]+=1
return(max(list.values()))
            
       


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

