a=input()
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
c=0
if len(a)!=18:
    print("Error")
else:
    for i in range(17):
        d=int(a[i])*b[i]
        c+=d
    d=c%11
    
    if a[17]=="X" and d==2:
        print("Correct")
    elif d==1 and a[17]=="0":
        print("Correct")
    elif d==0 and a[17]=="1":
        print("Correct")
    elif a[17]=="X" and d!=2:
        print("Wrong")
    elif d+int(a[17])==12:
        print("Correct")
    else:
        print("Wrong")


