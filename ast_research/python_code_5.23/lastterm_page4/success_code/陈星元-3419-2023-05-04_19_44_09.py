def calDegrees(a):
    ls=[]
    for x in a:
        n=a.count(x)
        ls.append(n)
    ls.sort(key=reverse)
    return ls[0]


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

