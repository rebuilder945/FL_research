n=input()
if len(n)!=18:
    print("Error")
else:
    a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    b=[int(n[i])*a[i] for i in range(17)]
    d=['1','0','X','9','8','7','6','5','4','3','2']
    c=sum(b)%11
    if d[c]!=n[17]:
        print("Wrong")
    else:
        print("Correct")        
