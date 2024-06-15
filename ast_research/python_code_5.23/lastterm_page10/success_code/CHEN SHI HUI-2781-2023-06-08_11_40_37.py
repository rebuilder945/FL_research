ic=input()
ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ls2=['1','0','X','9','8','7','6','5','4','3','2']
sum=0
if len(ic)!=18:
    print("Error")
else:
    for i in range(17):
        sum+=int(ic[i])*ls[i]
        yshu=sum%11
    if ls2[yshu]==ic[-1]:
        print('Correct')
    else:
        print('Wrong')


