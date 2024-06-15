def maxsum(l):
    b=[]
    k=0
    min_=0
    for i in range(int(len(l)/2)):
        b.append(l[k:(k+2)])
        k+=2
    for j in range(len(b)):
        min_+=min(b[j])
    return min_




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

