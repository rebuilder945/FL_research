def maxsum(y):
    a=0
    y.sort()
    for i in range(len(y)):
        if i%2==0:
           a+=y[i]
    return a  




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

