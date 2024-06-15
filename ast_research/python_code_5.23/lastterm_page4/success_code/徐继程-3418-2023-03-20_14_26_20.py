def maxsum(list):
    ls=[]
    length=int(int(len(list))/2+1)
    for i in range(length):
        a=min(list)
        list.remove(a)
        ls.append(a)
    return sum(ls) 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

