def maxsum(n):
    n.sort()
    a=[]
    for x in range(0,int(len(n)/2),2):
        a.append(min(n[x:x+1]))
    return sum(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

