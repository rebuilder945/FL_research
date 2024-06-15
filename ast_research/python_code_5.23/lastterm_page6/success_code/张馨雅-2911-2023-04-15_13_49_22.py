n=eval(input())
num=[]
while n>=1:
    a=(n+5)%10
    n//10#为什么我的n没有改变？
    num.append(a)
    if n<1:
        break
print(*num)
