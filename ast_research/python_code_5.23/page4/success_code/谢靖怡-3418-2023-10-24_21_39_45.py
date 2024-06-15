def maxsum(ls):
       ii=[]
       for i in range(len(ls)):
            a=min(ls)
            ii.append(a)
            ls.remove(a)
       s=0
       for x in ii[:2]:
             s=s+x
       return s




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

