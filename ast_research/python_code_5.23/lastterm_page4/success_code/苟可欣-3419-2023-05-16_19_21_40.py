def calDegrees(n):
    ls=[]
    for x in n:
        a=n.count(x)
        ls.append(a)
    return max(ls)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

