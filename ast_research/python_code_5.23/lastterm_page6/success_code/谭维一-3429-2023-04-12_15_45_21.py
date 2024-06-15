str=input()
ac,nc,sc,oc=0,0,0,0
for i in str:
    if "a"<=i<="z" or "A"<=i<="Z":
        ac+=1
    elif"0"<=i<="9":
        nc+=1
    elif i==" ":
        sc+=1
    else:
        oc+=1
print(ac,nc,sc,oc)
