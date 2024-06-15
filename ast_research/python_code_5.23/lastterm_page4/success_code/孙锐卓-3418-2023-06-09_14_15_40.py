def maxsum(a):
    a.sort()
    b=[]
    for i in range(len(a)):
        if i%2==0:
            b.append(i)
    return sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

