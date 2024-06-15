n=eval(input())
a=1
b=2
c=2
d=3
i=1
num=[2/1,3/2]
if n == 1:
    print("%.4f"%(2))
else:
    while i <n-1:
        a,b=b,a+b
        c,d=d,c+d
        num.append(d/b)
        i+=1
    print("%.4f"%(sum(num)))        

