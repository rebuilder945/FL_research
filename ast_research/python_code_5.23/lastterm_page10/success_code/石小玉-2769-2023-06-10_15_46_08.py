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
print(m)
for x in n:
    if x in Uplist:
        a=Uplist.index(x)
        print(Uplist[25-a],end="")
    elif x in Lowlist:
        b=Lowlist.index(x)
        print(Lowlist[25-b],end="")
    else:
        print(x,end="")
        

