# 高度反弹
h=eval(input())
N=eval(input())
c=[]
for i in range(1,N+1):
    if i==1:
        s=h
        c.append(s)
    else:
        s=h*2*(0.5**(i-1))
        c.append(s)
print("%.2f"% (sum(c)))
