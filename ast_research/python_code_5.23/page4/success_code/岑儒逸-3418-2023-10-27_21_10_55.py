def maxsum(mm):
    n=int(len(mm)/2)
    fin=[]
    for i in range(0,len(mm)/2-1):
        i=int(i)
        mm1=[mm[i],mm[i+n]]
        sums=sum(mm1)
        fin.append(sums)
    return min(fin)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

