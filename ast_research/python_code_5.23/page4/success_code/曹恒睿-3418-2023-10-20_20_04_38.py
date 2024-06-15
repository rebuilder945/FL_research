def maxsum(z):
    z=nums
    changdu = len(z)
    n=changdu/2
    xinshulie=[]
    while True:
          if len(xinshulie)==n:
                 break
          else:
                 zuixiaozhi=min(z)
                 xinshulie.append(zuixiaozhi)
                 z.remove(zuixiaozhi)
    he=sum(xinshulie)
    return he
          
    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

