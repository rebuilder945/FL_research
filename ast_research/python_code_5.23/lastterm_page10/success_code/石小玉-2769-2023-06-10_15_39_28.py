n=input()
m=n
Uplist=['A', 'B', 'C', 'D', 'E', \
'F', 'G', 'H', 'I', 'J', 'K', 'L',\
'M', 'N', 'O', 'P', 'Q', 'R', 'S',\
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Lowlist=['a', 'b', 'c', 'd', 'e',\
'f', 'g', 'h', 'i', 'j', 'k', 'l',\
'm', 'n', 'o', 'p', 'q', 'r', 's',\
't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in list(range(len(n))):
    for x in list(range(26)):
        if n[i]==Uplist[x]:
            n[i]=Uplist[27-x]
        elif n[i]==Lowlist[x]:
            n[i]==Lowlist[27-x]
        else:
            pass
print(m)
print(n)
        

