n=eval(input())-1
if n==1:
    print("%.2f"%h)
else:
    while n>0:
        eva+=eva*0.5*2
        eva*=0.5
        n-=1
    print("%0.2f"%eva)
