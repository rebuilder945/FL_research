def  maxsum(a):
    for x in a:
        a.remove(x)
        for y in a:
            c=min(x,y)
d=[c]
return d




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

