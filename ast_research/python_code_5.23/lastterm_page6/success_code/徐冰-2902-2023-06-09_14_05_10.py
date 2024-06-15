n=int(input())
ls=[2]
if n==1:
    print("2.0000")
else:
    for i in range(2,n+1):
        b=(i+i-1)/i
        ls.append(b)
c=sum(ls)
print("%.4f"%c)
    
