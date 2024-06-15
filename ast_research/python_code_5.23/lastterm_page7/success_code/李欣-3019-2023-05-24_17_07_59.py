name,english,python,math=input().split( )
ls=[float(english),float(python),float(math)]
ls=reversed(ls)
a,b,c=((' ').join(map(str,ls))).split( )
a=float(a)
b=float(b)
c=float(c)
avg=(a+b+c)/3
print(name,"%.2f"%a,"%.2f"%b,"%.2f"%c,"%.2f"%avg)
