n=eval(input())
ls=[]
a1=1
a2=2
if n ==1:
    print("%.4f"%2)
elif n == 2:
    print("%.4f"%3.5)
else:
    for i in range(n):
        a1,a2=a2,a1+a2
        


