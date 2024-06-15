def maxsum(nums):
    ls=[]
    sums.sort()
    for i in range(0,len(nums),2):
        ls.append(sums(i))
    return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

