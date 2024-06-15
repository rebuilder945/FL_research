lit={}
for i in eval(input()):
    if i not  in lit:
         lit[i]=1
    else:
         lit[i]+=1
print(max(lit.values()))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

