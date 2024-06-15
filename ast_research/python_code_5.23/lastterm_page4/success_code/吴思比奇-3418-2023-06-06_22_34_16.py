def maxsum(num):
    len=len(num)
    num.revese()
    a=num[0,len+1,2]
    sum=sum(a)
    return sum
    remain()




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

