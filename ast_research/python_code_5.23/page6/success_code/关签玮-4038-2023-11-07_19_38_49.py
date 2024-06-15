a=list(input())
ycount,scount,kcount,tcount=0,0,0,0
for i in a:
    if "a"<=i<="z"or"A"<=i<="Z":
        ycount+=1
    elif"0"<=i<="9":
        scount+=1
    elif i==" ":
        kcount+=1
tcount=len(a)-ycount-scount-kcount
print(ycount,scount,kcount,tcount,end=" ")
