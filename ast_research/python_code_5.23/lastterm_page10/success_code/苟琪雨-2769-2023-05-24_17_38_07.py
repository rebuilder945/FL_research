uplist=['A','B','C','D','E','F',"G",'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',"x",'Y','Z']
lolist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str=list(input())
strc=''.join(str)
for i in range(len(str)):
    if str[i] in uplist:
        n=uplist.index(str[i])
        str[i]=uplist[25-n]
    if str[i] in lolist:
        n=lolist.index(str[i])
        str[i]=lolist[25-n]
print(strc)
print("".join(str))
