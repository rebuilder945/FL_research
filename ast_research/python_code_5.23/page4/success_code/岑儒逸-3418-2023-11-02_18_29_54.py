def maxsum(ls):
    ls1=[]
    ls.sort()
    n=len(ls)/2
    for i in range(0,len(ls)-1,2):
        i += 1
        ls1.append(ls[i])
    return sum(ls1)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

