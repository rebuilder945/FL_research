def calDegrees(a):
    b=a.count(0)
    c=a.count(1)
    d=a.count(2)
    e=a.count(3)
    f=a.count(4)
    g=a.count(5)
    h=a.count(6)
    i=a.count(7)
    j=a.count(8)
    k=a.count(9)
    l=a.count(0)
    p=max(b,c,d,e,f,g,h,i,j,k,l)
    return p


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

