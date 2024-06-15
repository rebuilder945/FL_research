def calDegrees(nums):
    m=0
    ls=[]
    for x in nums:
        m=num.count(x)
        ls.append(m)
    ls.sort()
    print(ls[-1])
        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

