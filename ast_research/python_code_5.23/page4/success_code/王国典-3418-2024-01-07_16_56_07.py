def maxsum(ls):
    ls.sort()
    min_sum=0
    for i in range(0,len(ls),2):
        min_sum+=ls[i]
    return min_sum
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

