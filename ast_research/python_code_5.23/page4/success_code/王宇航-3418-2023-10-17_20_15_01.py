ls=eval(input())
N=eval(innpu())
ls2=ls*N
ls3=[x*x for x in ls2]
ls4=[]
for x in ls3:
    if x not in ls4:
        ls4.append(x)
print(ls4)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

