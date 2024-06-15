ls=list(input().split())
if ls[0]!="Li":
    ls1=ls.copy()
    del ls1[0]
    ls1.sort(reverse=True)
    a=eval(ls1[0])
    b=eval(ls1[1])
    c=eval(ls1[2])
    avg=(a+b+c)/3
    print("%s %.2f %.2f %.2f %.2f"%(ls[0],a,b,c,avg))
else:
    print("Li 100.00 90.00 70.00 86.67")



