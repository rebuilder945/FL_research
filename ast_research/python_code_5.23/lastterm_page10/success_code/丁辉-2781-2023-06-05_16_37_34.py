a=input()
if len(a)!=18:
    print("Error")
else:
    xlst=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    b=0
    for i in range(0,17):
        b+=(int(a[i])*xlst[i])
    n=b%11
    if a[17]=='X':
        if n==2:    
            print("Correct")
        else:
            print("Wrong")
    if a[17]!='X':
        if int(a[17])==(12-n)%11:
            print("Correct")
        else:
            print("Wrong")
