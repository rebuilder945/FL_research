def maxsum(a):
    sum=0
    l=len(a)/2
    a.sort()
    for x in range (int(l)):
        a.pop()
        sum+=a.pop() 
    return sum   




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

