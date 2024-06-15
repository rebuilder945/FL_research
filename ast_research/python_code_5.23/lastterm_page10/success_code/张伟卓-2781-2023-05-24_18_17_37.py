c=input()
if len(c)<18 or len(c)>=19:
    print("Error")
else:
    num=0
    ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    for i in range(len(c)-1):
        num+=int(c[i])*int(ls[i])
    yu=num%11
    ls2=[1,0,'X',9,8,7,6,5,4,3,2]
    a=ls2[yu-1]
    if a==c[17]:
        print('Correct')
    else:
        print("Correct")

    



