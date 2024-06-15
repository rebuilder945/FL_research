a=input()
if len(a)!=18:
    print("Error")
else:
    b=a[-1]
    z=0
    a=list(a)
    m=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for i in range(len(m)):
        z+=int(a[i])*m[i]
    z=z%11
    if z==2:
        q="X"
    else:
        q=(12-z)%11
    if str(q)==b:
        print("Correct")
    else:
        print("Wrong")
