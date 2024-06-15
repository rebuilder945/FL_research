id=input()
if len(id)!=18:
    print("Error")
else:
    xishu=[7,9,1,0,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    yushu=[0,1,2,3,4,5,6,7,8,9,10]
    jiaoyan=[1,2,"X",9,8,7,6,5,4,3,2]
    ls=0
    for i in range(17):
        a=int(id[i])*xishu[i]
        ls+=a
        ys=ls%11

        for x in range(11):
            if ys!=yushu[x]:
                break
            elif ys==yushu[x]:
                id[17]==jiaoyan[x]
                print("Correct")
            else:
                print("Wrong")

