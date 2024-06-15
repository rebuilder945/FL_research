a=input()
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
c=0
if len(a)!=18:
    print("Error")
else:
    for i in range(17):
        c+=a[i]*b[i]
    if a[18]!=c:
        print('Error')
    else:
        print('Correct')
