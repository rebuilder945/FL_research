def calDegrees(a):
    a1=[]
    for b in a:
        c = a.count(b)
        a1.append(c)
      return max(a1)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

