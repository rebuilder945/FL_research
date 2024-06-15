a=input()
b='79X584216379X5842'
#d=[i for i in range(11)]
c=0
if len(a)!=18:
    print('Error')
    end
else:
    for i in range(len(a)-1):
        if a[i]=='X':
            if b[i]=='X':
                c+=100
            else:
                c+=10*int(b[i])
        else:
            if b[i]=='X':
                c+=10*int(a[i])
            else:
                c+=int(b[i])*int(a[i])
    n=c%11
    m=(12-n)%11
    if a[-1]=='X':
        if m==10:
            print('Correct')
        else:
            print('Wrong')
    else:
        if int(a[-1])==m:
            print('Correct')
        else:
            print('Wrong')
