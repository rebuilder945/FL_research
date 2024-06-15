def sumlist(L):
    sum=0
    for i in range(len(L)):
       if (type(L[i]) == type([])):
          sum=sum+sumlist(L[i])
       else:
          sum=sum+L[i]
    return sum

nums = eval(input())
sumv = sumlist(nums)
print(sumv)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

