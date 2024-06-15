a=input()
l,s,d,o=0,0,0,0
for x in s:
    if x.isalpha():
        l+=1
    elif x.isspace():
        s+=1
    elif x.isdigit():
        d+=1
    else:
        o+=1
print(l,s,d,o)
            

            


