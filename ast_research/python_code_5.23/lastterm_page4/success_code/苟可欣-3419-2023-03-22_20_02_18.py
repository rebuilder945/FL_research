def calDegrees(num):
    a=[]
    for x in num:
        b=num.count(x)
        a.append(b)
    return max(a)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

