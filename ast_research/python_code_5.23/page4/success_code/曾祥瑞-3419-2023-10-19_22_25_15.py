def calDegrees(nums):
    dic={}
    for x in nums:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
    max(dic.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

