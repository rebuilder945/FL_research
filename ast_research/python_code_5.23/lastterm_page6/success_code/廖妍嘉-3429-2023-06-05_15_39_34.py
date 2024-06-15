n=input()
e,k,m,o=0,0,0,0
for i in n:
    if "a"<= i <="z" or "A"<= i <= "Z":
        e+=1
    elif "0"<=i<="9":
        m+=1
    elif i==" ":
        k+=1
    else:
        o+=1
print(e,k,m,o) 
