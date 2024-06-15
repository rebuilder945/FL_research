h=eval(input())
N=eval(input())
res=0
while N>1:
    res=h*0.5
    s=h+res
    h=h/2
    N=N-1
res=s
print("%.2f",res)
    

