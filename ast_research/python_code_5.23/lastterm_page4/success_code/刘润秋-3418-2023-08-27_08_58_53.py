def maxsum(y):
    y.sort()
    long=len(y)
    list=range(1,long+1,2)
    eva=0
    for x1 in list:
          eva=eva+x[x1-1]
    return eva




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

