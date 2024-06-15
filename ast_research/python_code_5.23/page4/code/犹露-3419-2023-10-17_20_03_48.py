def calDegrees(n)：
a = []
for i in n:
    i_count = n.count(i)
    a.append(i_count)
c= max(a)
return c



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

