def maxsum(a):
      c=sorted(a)
      b=0
      number=c[0:len(c)+1:2]
      for x in number:
            b+=x
      return b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

