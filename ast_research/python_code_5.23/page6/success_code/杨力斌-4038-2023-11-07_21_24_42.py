a = input()
zimu = 0
shuzi = 0
kongge = 0
ii = 0
for i in a:
    if i.isalpha:
        zimu +=1
    elif i.isdigit:
        shuzi +=1
    elif i.isspace:
        kongge +=1
    else:
        ii +=1
print(zimu,kongge,shuzi,ii)
