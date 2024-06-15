dic={}
for i in nums:
    if i not in dic:
         dic[i]=1
    else:
         dic[i]+=1
return max(dic.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

