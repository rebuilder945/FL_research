a=input()
if len(a)!=18:
    print("Error")
else:
    b=0
    c=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for i in range(17):
        if a[i]=="X":
            b+=10*c[i]
        else:
            b+=eval(a[i])*c[i]
    if a[-1]=="X":
        if 10==(12-b%11)%11:
            print("Correct")
        else:
            print("Wrong")
    
    elif eval(a[-1])==(12-b%11)%11:
        print("Correct")
    else:
        print("Wrong")
        

    



