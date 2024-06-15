def maxsum(a):
    sum=0;
    a.sort(reverse=False);
for i in range(len(a));
    if i%2==0:
        sum+=a[i];
    return sum;




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

