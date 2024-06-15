def maxsum(ls):
    ls1=[]
    ls.sort()
    n=int(len(ls)/2)
    for i in range(1,n):
        i=i*2+1
        ls1.append(ls[i])
    return sum(ls1)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

