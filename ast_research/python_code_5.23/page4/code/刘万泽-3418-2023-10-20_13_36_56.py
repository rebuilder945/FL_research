def maxsum:
       for a in nums:
             for b in nums:
                   t=[ ]
                  t.append(a+b)
       return max(t)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

