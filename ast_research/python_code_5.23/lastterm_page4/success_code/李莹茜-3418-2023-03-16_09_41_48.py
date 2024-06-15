def maxsum(mminhe):
    fuben=[]
    k=0
    minhe=0
    for i in range(0,len(nums),2):
        fuben.append(nums[k:(k+2)])
        k+=2
    for j in range(len(fuben)):
        minhe+=min(fuben[j])
    return max(mminhe)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

