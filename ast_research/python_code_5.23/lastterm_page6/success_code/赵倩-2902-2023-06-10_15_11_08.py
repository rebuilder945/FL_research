a=eval(input())
l1=[2,3]
l2=[1,2]
s=3.5
if a>2:
    for i in range(a-2):
        b=l1[-2]+l1[-1]
        c=l2[-2]+l2[-1]
        s+=b/c
        l1.append(b)
        l2.append(c)
    print("%.4f"%s)
elif a==1:
    print("2.0000")
elif a==2:
    print("3.5000")














