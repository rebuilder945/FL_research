a=input()
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
c=0
e=['1','0','X','9','8','7','6','5','4','3','2']
if len(a)!=18:
    print("Error")
else:
    for i in range(17):
        c+=int(a[i])*b[i]
        d=c%11
        f=e[d]
    if a[17]!=f:
        print('Wrong')
    else:
        print('Correct')
