a=int(input())
b=int(input())
if b>1:
    s=10
    for i in range(b-1):
        s=s+a/(2**i)
        
        
else:
    s=a
print("%.2f"%s)


                

