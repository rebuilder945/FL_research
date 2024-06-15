def calDegrees(a):
    c = []
    for x in a:
        b=a.count(x)
        c.append(b)
    print(max(c))
 



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

