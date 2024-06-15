def fufu(a):    
    d=len(a)
    for x in a:
        b=a.count(x)
        c=[b/d]

e=fufu(eval(input))
print(e)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

