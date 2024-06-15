def maxsum(x): #[1,4,3,2]
    x.sort() #[1,2,3,4,5,6,7,8]
    return sum(x[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

