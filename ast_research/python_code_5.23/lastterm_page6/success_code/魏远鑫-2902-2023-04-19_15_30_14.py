n=eval(input())
ls=[]
a1=1
a2=2
b1=2
b2=3
ls=[3.5]
if n ==1:
    print("%.4f"%2)
elif n == 2:
    print("%.4f"%3.5)
else:
    for i in range(n-2):
        b1,b2=b2,b2+b1
        a1,a2=a2,a2+a1
        c=b2/a2
        ls.append(c)
print("%.4f"%sum(ls))

        



