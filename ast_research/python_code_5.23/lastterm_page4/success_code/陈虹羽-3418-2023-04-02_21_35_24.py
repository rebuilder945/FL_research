def maxsum(num):
    b=[]
    num.sort()
    c=len(num)
    for i in range(0,c,2):
      b.append(num[i])
    return(sum(b))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

