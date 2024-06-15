def calDegrees(n):
    ls=input()
    ls1=[]
    m=0
    for i in ls:
        m=ls.count(i)
        ls1.append(i)
    ls1.sort()
    print(ls[-1])


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

