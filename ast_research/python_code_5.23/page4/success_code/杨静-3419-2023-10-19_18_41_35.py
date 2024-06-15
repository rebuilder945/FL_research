def calDegrees(lis):
    b=[]
    for x in lis:
        b.append(lis.count(x))
    return max(b)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

