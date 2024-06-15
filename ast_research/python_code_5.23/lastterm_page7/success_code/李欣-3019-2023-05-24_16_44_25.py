name,english,python,math=input().split( )
dic={}
a=float(english)
b=float(python)
c=float(math)
ls=[a,b,c]
ls=reversed(ls)
avg=sum(ls)/3
print(eval(name),"%.2f"%ls[0],"%.2f"%ls[1],"%.2f"%ls[2],"%.2f"%avg)
