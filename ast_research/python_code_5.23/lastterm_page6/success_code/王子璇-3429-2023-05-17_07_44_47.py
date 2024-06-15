s=input()
english,kongge,shuzi,qita=0,0,0,0
for x in s:
    if x.isalpha():
        english+=1
    elif x.isdigit():
        shuzi+=1
    elif x==' ':
        kongge+=1
    else:
        qita+=1
print(english,kongge,shuzi,qita)
