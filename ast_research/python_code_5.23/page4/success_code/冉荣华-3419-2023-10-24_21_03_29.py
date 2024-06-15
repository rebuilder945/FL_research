def calDegrees(nums):
    x=[]
    for i in nums:
        if i not in x:
            m=1
            x.append(m)
        else:
            m+=1
            x.apend(m)
    return max(x)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

