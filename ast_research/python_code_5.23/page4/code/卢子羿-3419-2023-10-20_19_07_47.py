   def calDegrees(nums):
    a={}
    for i in nums:
        if i not in a:
            a[i]=1
        else:
             a[i]+=1
    return max(a.values())



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

