a=input()
if len(a)!=18:
    print("Error")
else:
    xlst=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    n=0
    for i in range(0,17):
        n+=(int(a[i])*xlst[i])%11
    if n==2 and a[17]=='X':
        print("Correct")
    if n!=2 and int(a[17])==(12-n)%11:
        print("Correct")
    else:
        print("Wrong")
