def main(n):
    a=1
    b=2
    s=0
    for i in range(n):
        s+=b/a
        a,b=b,a+b
    return("%.4f"%(s))
        





n=eval(input())
print(main(n))




    





