s=input()
char,space,num,other=0,0,0,0
for x in s:
    if "a"<=x<="z" or "A"<=x<="Z":
        char+=1
    elif x==" ":
        space+=1
    elif "0"<=x<="9":
        num+=1
    else:
        other+=1
print(char,space,num,other )
            


