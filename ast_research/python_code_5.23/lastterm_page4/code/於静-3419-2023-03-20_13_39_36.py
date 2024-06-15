d={}
for i in eval(input()):
     if i not in d:
     d[i]=1
     else:
     d[i]+=1


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

