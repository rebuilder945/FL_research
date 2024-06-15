def maxsum(l):
       l.sort()
       ilen=len(l)
       n=0
       for i in range(ilen):
            if i%2==0:
                n=n+l[i]
        return n




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

