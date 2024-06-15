a=input()
if len(a)!=18:
    print("Error")
else:
    n=(7*a[0]+9*a[1]+10*a[2]+5*a[3]+8*a[4]+4*a[5]+2*a[6]+1*a[7]+6*a[8]+3*a[9]+7*a[10]+9*a[11]+10*a[12]+5*a[13]+8*a[14]+4*a[15]+2*a[16])%11
    lastn=['1','0','X','9','8','7','6','5','4','3','2']
    lasti=n%11
    if lastn[lasti]==a[-1]:
        print("correct")
    else:
        print("wrong")
    
