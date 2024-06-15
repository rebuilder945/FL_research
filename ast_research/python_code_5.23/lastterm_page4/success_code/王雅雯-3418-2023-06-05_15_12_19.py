def maxsum(y):
    sum=0;
    y.sort(reverse=False);
    minv=y[::2]
    sum=sum(minv)
    return sum;




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

