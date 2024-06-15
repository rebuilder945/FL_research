words=input()
listword=list(words)
daxie=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
xiaoxie=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rdaxie=daxie[::-1]
rxiaoxie=xiaoxie[::-1]
result=[]
for i in listword:
    if i.isalpha():
        if i.islower():
            location=xiaoxie.index(i)
            result.append(rxiaoxie[location])
        else:
            location=daxie.index(i)
            result.append(rdaxie[location])
    else:
        result.append(i)
for x in result:
    print(x,end="")
