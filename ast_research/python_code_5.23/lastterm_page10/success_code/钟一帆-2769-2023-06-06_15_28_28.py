mima=input()
mimaben1='abcdefghijklmnopqrstuvwxyz'
mimaben2=mimaben1.upper()
guo=''
for i in mima:
    if i.isalpha():
        if i.islower():       
            for x in range(len(mimaben1)):
                if mimaben1[x]==i:
                    guo+=mimaben1[25-x]
        if i.isupper():       
            for x in range(len(mimaben2)):
                if mimaben2[x]==i:
                    guo+=mimaben2[25-x]   
    else:guo+=i           
print(mima)
print(guo)                    
