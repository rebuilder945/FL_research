 def calDegrees(nums)
    a=[]
    for i in nums:
        if i not in a:
          a.append(i)
        else:
          break
    b=0
    for i in a:
        c=nums.count(i)
        if c>b:
            b=c
        else:
          break
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

