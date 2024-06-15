a=input()
sum=0
if len(a)!=18:
    print('Error')
else:
    sum=7*int(a[0])+9*int(a[1])+10*int(a[2])+5*int(a[3])+8*int(a[4])+4*int(a[5])+2*int(a[6])+int(a[7])+6*int(a[8])+3*int(a[9])+7*int(a[10])+9*int(a[11])+10*int(a[12])+5*int(a[13])+8*int(a[14])+4*int(a[15])+2*int(a[16])
    m=12-sum%11
    print(m)
    if m==10 and a[17]=='X':
        print('Correct')
    elif str(m)==a[17]:
        print('Correct')
    else:
        print('Wrong')

