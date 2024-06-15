h=eval(input())
n=eval(input())
num=0
if n==1:
    num=h
else:
    num+=h
    H=h
    for x in range(2,n+1):
        H=H*0.5
        num+=H*2
print("%.2f"%num)
