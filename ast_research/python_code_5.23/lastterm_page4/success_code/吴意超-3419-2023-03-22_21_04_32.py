def z(n):
    m = 0
    for i in n:
        if(m < n.count(i)):
            m = n.count(i)
    return m

n = eval(input())
d = z(n)
print(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

