a=[5,2,6,7,2,9,5,8]
b=[]
k=0
min_ = 0
for i in range(int(len(a)/2)):
    b.append(a[k:(k+2)])
    k+=2
for j in range(len(b)):
    min_ += min(b[j])
print(min_)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

