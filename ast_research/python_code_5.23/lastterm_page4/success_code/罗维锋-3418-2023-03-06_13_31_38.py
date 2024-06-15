def maxsum(x):
    x.sort()
    s=[]
    for i in range(0,len(x),2):
        s.append(min((x[i],x[i+1])))
    return sum(s)   




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

