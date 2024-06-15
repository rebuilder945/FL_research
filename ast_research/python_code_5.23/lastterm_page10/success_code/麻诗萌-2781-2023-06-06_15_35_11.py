n=list(input())
if len(n)==18:
    s=0
    lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    lst2=[0,1,2,3,4,5,6,7,8,9,10]
    lst3=[1,0,10,9,8,7,6,5,4,3,2] 
    for i in range(len(n)):
        if n[i]=="X":
            n[i]=10
        else:
            n[i]=int(n[i])
        if i<17:
            s=s+n[i]*lst1[i]   
    n=s%11
    m=(12-n)%11
    x=lst2.index(n)
    if lst3[x]==m:
        print("Correct")
    else:
        print("Wrong")
else:
    print("Error")


    
