def calDegrees(nums):
    dict={}
    for i in nums:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    return max(dic.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

