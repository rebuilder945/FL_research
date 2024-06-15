def maxsum(list):
    list.sort(reverse=True)
    ls=[]
    length=int(int(len(list))/2)
    for i in range(length):
        a=list.pop()
        ls.append(a)
        list.pop()
    return sum(ls) 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

