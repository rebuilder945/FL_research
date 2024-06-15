a=eval(input())
for x in a:
    b=a.count(x)
    c=[b/len(a)]
print(max(c))



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

