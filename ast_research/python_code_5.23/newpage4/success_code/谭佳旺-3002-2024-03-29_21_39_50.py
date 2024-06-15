a =eval(input())
b =sum(a)/len(a)
if b%1==0:
    b=int(b)
    print(b)
if b%1!=0:
    print("%.2f"%b)
