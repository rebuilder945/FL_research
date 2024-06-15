import random
ls=[]
random.shuffle(ls)
min_ls=0
max_ls=0
d=[]
for i in range(0,len(ls),2):
    print(ls[i],ls[i+1])
    min_ls=min_ls+min(ls[i],ls[i+1])
    d.append(min_ls)
maxsum(nums)=max(d)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

