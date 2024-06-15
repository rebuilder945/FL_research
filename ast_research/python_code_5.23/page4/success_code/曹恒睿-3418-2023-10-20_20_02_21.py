def maxsum(z):
    yuanshulie=nums
    changdu = len(yuanshulie)
    n=changdu/2
    xinshulie=[]
    while True:
          if len(xinshulie)==n:
                 break
          else:
                 zuixiaozhi=min(yuanshulie)
                 xinshulie.append(zuixiaozhi)
                 yuanshulie.remove(zuixiaozhi)
    he=sum(xinshulie)
    return he
          
    





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

