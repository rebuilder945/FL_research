ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ID=input()
if len(ID)!=18:
    print("Error")
else:
    sum=0
    n=0
    while n<=16:
        sum+=int(ID[n])*int(ls[n])
        n+=1
    rushu=sum % 11
    ls2=['1','0',"X",'9','8','7','6','5','4','3','2']
    if ls2[rushu]!=ID[17] :
        print('Wrong')
    else:
        print("Correct")


