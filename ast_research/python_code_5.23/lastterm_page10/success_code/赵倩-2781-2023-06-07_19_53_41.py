a=list(input())
la=len(a)
d={}
d[0]=1
d[1]=0
d[2]=10
d[3]=9
d[4]=8
d[5]=7
d[6]=6
d[7]=5
d[8]=4
d[9]=3
d[10]=2
if la!=18:
    print("Error")
else:
    if a[17]=="x":
        a[17]=10
    b=eval(a[0])*7+eval(a[1])*9+eval(a[2])*10+eval(a[3])*5+eval(a[4])*8+eval(a[5])*4+eval(a[6])*2+eval(a[7])*1+eval(a[8])*6+eval(a[9])*3+eval(a[10])*7+eval(a[11])*9+eval(a[12])*10+eval(a[13])*5+eval(a[14])*8+eval(a[15])*4+eval(a[16])*2
    n=b%11

    if d[n]==eval(a[17]):
        print("Correct")
    else:
        print("Wrong")


            

