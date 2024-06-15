def maxsum(nums):
    a=[]
    b=[]
    j=0
    min=0
    for i in range(int(len(a)/2)):
        b.append(a[k:(k+2)])
        k+=2
    for j in range(len(b)):
        min+=min(b[j])





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

