st=list(input())
eng=['a','b','c','d','e','f','g',\
     'h','i','j','k','l','m','n',\
        'o','p','q','r','s','t','u','v'\
            'w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',\
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=['0','1','2','3','4','5','6','7','8','9']
en=0
space=0
nu=0
oth=0
for x in st:
    if x in eng:
        en=1+en
    elif x in num:
        nu=1+nu
    elif x==" ":
        space=1+space
    else:
        oth=1+oth
print(en,space,nu,oth)




