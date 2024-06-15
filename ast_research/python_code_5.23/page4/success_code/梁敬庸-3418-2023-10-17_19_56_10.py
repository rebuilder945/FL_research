
def maxsum(n):
    n.sort()
    b=[]
    d=len(n)/2
    for i in range(d):
        i=1+2*i
        b.append(n[i])
    return sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

