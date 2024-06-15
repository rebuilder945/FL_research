height=eval(input())
N=eval(input())
res=0
while N>1:
    res+=height*(3/2)
    height=height/2
    N-=1
    res+=height
print("%.2f"%res)
