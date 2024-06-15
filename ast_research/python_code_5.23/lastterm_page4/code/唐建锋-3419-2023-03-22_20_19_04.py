ls=list()
for i in ls:
    if i not in ls.keys():
    ls[i]=ls.count(i)
print(ls)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

