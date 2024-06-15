x=input()
zimu=0
shuzi=0
space=0
zifu=0
for i in x:
    if int(ord(i)) in list(range(65,123)):
        zimu+=1
    elif int(ord(i)) in list(range(48,58)):
        shuzi+=1
    elif int(ord(i))==32:
        space+=1
    else:
        zifu+=1
print(zimu,space,shuzi,zifu)
    

