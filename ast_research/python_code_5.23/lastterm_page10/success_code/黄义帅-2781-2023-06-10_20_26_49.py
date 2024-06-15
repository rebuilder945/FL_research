ID=input()
if len(ID)!=18:
    print("Error")
else:
    if ID[17]=="X":
        ID_Check=10
    else:
        ID_Check=int(ID[17])
    XS=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    ID_JY=[1,0,10,9,8,7,6,5,4,3,2]
    sum=0

    for i in range(len(XS)):
        sum+=XS[i]*int(ID[i])
    n=sum%11
    if ID_JY[n]==ID_Check:
        print("Correct")
    else:
        print("Wrong")
    





