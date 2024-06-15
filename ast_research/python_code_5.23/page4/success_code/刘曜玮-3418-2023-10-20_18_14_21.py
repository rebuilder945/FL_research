def maxsum(nums):
    list=[]
    n=1
    nums.sort(reverse=True)
    for x in nums:
        if n%2==0:
            list.append(x)
        n+=1
    all = sum(list)
    return all





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

