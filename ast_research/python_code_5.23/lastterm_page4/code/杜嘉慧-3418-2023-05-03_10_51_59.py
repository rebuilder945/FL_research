def maxsum(m):
       h=[]
       n=len(m)
       m.sort()
       return sum(m[::2])
        for i in m[::2]:
             h.append(i)
        return sum(h)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

