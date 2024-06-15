def maxsum(ls1):
    n = len(ls1)
    ls1.sort()
    zc = (n+1)/2
    i,k = 0,0
    sum = 0
    while(k<zc-1):
        sum+=ls1[i]
        i+=2
        k+=1
    return(sum)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

