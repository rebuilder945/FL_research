def maxsum(r):
    n2=len(r)
    n=n2/2
    t=-n-1
    k=list(r)
    k.sort(reverse=True)
    print(k)
    p=0
    for i in k[-1:t]:
        p+=i
    return p




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

