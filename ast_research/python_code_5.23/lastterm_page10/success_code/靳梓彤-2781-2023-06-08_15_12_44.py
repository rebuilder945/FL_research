id=input()
if len(id)!=18:
    print("Error")
elif len(id)==18:
    xishu=[7,9,1,0,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    ls=0
    for i in range(17):
        a=int(id[i])*xishu[i]
        ls+=a
    ys=ls%11
    m=(12-ys)%11
    if str(m)!=id[-1] and m!=10:
        print("Wrong")
    elif m==10 and id[-1]=="X":
        print("Correct")
    elif m!=10 and str(m)==id[-1]:
        print("Correct")
    elif m==10 and id[-1]!="X":
        print("Wrong")




