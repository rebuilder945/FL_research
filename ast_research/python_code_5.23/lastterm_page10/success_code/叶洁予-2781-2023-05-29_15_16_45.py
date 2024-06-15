ID=input()
if len(ID)!=18:
    print("Error")
else:
    ID_check=ID[17]
    W=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    ID_CHECK=['1','0','X','9','8','7','6','5','4','3','2']
    ID_aXw=0
    for i in range(len(W)):
        ID_aXw=ID_aXw+int(ID[i])*W[i]
    ID_Check=ID_aXw % 11
    if ID_check!=ID_CHECK[ID_Check]:
        print("Wrong")
    else:
        print("Correct")
