a=input()
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
c=0
if len(a)!=18:
    print("Correct")
else:
    for i in range(10):
        c+=int(a[i])*b[i]
    d=c%11
    if d==int(a[10]):
        print("Correct")
    else:
        print("Error")


