s=input()
daxie=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
xiaoxie=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s1=list(s)
s2=s1.copy()
for i in range(0,len(s1)):
    if s1[i] in daxie:
        a=daxie.index(s1[i])
        s2[i]=daxie[24-a+1]
    elif s1[i] in xiaoxie:
        a=xiaoxie.index(s1[i])
        s2[i]=xiaoxie[24-a+1]
    else:
        pass
print(s)
print(''.join(s2))
