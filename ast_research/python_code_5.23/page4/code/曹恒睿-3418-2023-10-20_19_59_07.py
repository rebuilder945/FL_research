def maxsum(z):
    yuanshulie=eval(input())
    changdu = len(yuanshubiao)
    n=changdu/2
    xinshulie=[]
    while True:
          if lenth(xinshulie) =n:
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

