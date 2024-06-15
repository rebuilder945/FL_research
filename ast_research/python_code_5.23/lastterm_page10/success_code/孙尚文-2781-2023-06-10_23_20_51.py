a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
b=input()
print(b)
c=0
if len(b)==18:
    for i in range(17):
        c+=int(b[i])*a[i]
    d=c%11
    m=(12-d)%11
    if m==10 and b[-1]=="X":
        print("Correct")
    elif m==b[-1]:
        print("Correct")
    else:
        print("Wrong")
else:
    print("Error")
