def maxsum(L=[]):
    L.sort()
    List=[]
    for x in L:
        if L.index(x) % 2 == 0  :
            List.append(x) 
        else:
            pass
    return  sum(List)   




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

