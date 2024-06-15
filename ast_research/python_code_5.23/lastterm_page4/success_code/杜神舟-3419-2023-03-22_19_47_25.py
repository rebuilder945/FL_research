a=eval(input())
d=len(a)
for x in a:
    b=a.count(x)
    c=[b/d]
print(max(c))



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

