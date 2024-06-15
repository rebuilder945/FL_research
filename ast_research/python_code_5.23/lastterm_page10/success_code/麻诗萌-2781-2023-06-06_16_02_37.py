n=list(input())
if len(n)==18:
    s=0
    lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    dic2={0:1,1:0,2:10,3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:2}
    for i in range(len(n)):
        if n[i]=="X":
            n[i]=10
        else:
            n[i]=int(n[i])
        if i<17:
            s=s+n[i]*lst1[i]   
    t=s%11
    if dic2[t]==n[-1]:
        print("Correct")
    else:
        print("Wrong")
else:
    print("Error")


    
