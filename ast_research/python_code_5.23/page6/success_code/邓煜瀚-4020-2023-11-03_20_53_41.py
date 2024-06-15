h=eval(input())
N=eval(input())
res=[]
while N>1:
    res+=h*3/2
    h=h/2
    N-=1
res+=h
print("%.2f"%res)
