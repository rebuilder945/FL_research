a = input()
zimu = 0
shuzi = 0
kongge = 0
ii = 0
for i in a:
    print(i)
    if i.isspace():
        zimu +=1
    elif i.isdigit():
        shuzi +=1
    elif i.isalpha():
        kongge +=1
    else:
        ii +=1
print(zimu,kongge,shuzi,ii)
