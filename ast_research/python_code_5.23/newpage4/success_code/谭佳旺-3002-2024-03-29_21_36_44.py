a =eval(input())
b =sum(a)/len(a)
if b%1==0:
    c=b//1
    print(c)
if b%1!=0:
    print("%.2f"%b)
