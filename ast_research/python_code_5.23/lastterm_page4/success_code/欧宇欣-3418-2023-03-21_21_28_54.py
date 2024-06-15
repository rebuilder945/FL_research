def maxsum(x):
    x=nums
    y=[]
    k=0
    maxsum = 0
    for i in range(int(len(x)/2)):
        y.append(x[k:(k+2)])
        k+=2
    for j in range(len(y)):
        maxsum +=min(y[j])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

