'''def calDegrees(nums):
    for x in nums:
        m=[]
        m.append(nums.count(x))
    return max(m)
nums  =  eval(input())
d=calDegrees(nums)  #调用自定义函数
print(d)'''

'''def maxsum(nums):
    nums.sort()
    n=nums[::2]
    return sum(n)
nums  =  eval(input())
v  =  maxsum(nums)
print(v)'''

'''def Fibonacci(num,n):
    for n in range(n-2):
        m=num[-1:-3:-1]
        a=sum(m)
        num.append(a)
    return num[-1]
num=[1,1]
n=int(input())
print(Fibonacci(num,n))'''

'''m=eval(input())
n=[]
for i in range(len(m)):
    if m[i:].count(m[i])==1: n.append(m[i])
print(n)'''

'''m=eval(input())
n=list(range(1,m+1))
a=n.pop(0)
n.append(a)
print(n)'''

'''def sushu(y):
    x=[]
    for i in y:
        if i>=2:
            for j in range(2,i,1):
                if i%j==0:
                    break
            else:
                x.append(i)
    print(x)
sums=eval(input())
sushu(sums)'''

m=eval(input())
m.sort()
m.reverse()
s=''
for x in m:
    s=s+str(x)
print(int(s))

    
