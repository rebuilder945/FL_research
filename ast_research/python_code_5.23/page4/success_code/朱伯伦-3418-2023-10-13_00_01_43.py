def maxsum(list):
    sum=0
    list.sort(reserve=False)
    for i in range(len(list)):
        if i%2==0:
            sum+=list[i]
        return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

