s=input()
l=['1','0','X','9','8','7','6','5','4','3','2']
if len(s)==18:
    m=(7*int(s[0])+9*int(s[1])+10*int(s[2])+5*int(s[3])+8*int(s[4])+4*int(s[5])+2*int(s[6])+int(s[7])+6*int(s[8])+3*int(s[9])+7*int(s[10])+9*int(s[11])+10*int(s[12])+5*int(s[13])+8*int(s[14])+4*int(s[15])+2*int(s[16]))%11
    n=(12-m)%11
    if s[-1]==l[n]:
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')

