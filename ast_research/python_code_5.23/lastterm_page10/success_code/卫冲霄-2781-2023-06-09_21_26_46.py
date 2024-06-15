ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ls1=[1,0,"X",9,8,7,6,5,4,3,2]
id=input()
if len(id)!=18:
    print("Error")
else:
    sum=0
    for i in range(17):
        sum+=int(id[i])*ls[i]
    yushu=sum%11
    if ls1[yushu]==id[-1]:
        print("Correct")
    else:
        print("Wrong")






