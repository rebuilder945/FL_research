def maxsum(list):
    list2=[]
    k=0
    min_=0
    for i in range (int(len(list)/2)):
        list2.append(list[k:(k+2)])
        k+=2
    for x in range(len(list2)):
        min_+=min(list2[x])
    return min_




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

