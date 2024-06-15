l = eval(input())
a = 0
for i in l:
    s=l.count(i)
    # a=s
    if s>=a :
        a = s
print(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

