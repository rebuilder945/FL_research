from re import I


def A(a):
    i=1
    b=2
    s=0
    for e in range(a):
        s+=b/i
        b,i=i+b,b
    return(s)
a=eval(input())
print("%.4f"%A(a))
        
    
