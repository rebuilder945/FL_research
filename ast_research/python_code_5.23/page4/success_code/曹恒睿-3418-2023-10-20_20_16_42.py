def maxsum(z):
    changdu = len(z)
    n=changdu/2
    xinshulie=[]
    while True:
          if len(xinshulie)==n:
                 break
          else:
                 zuidazhi=max(z)
                 z.remove(zuidazhi)
                 zuidazhi2=max(z)
                 xinshulie.append(zuidazhi2)
                 z.remove(zuidazhi2)
    he=sum(xinshulie)
    return he





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

