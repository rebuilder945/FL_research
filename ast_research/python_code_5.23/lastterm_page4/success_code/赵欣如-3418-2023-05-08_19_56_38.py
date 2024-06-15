def maxsum(x):
    x.sort()
    a=0
    for i in x:
        if x.index(i)%2==0:
             a+=i
  
        else:
             pass
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

