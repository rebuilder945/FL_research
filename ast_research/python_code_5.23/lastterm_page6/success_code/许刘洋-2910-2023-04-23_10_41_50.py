h=input()
n=input()
num=0
if n==1:
    num=h
else:
    num+=h
    for x in range(2,n+1):
        H=h*0.5**(x-1)
        num+=H*2
print("%.2f"%num)
