ls=input()
ls1,ls2,ls3,ls4=0,0,0,0
for i in ls:
    if "a"<=i<="z" or "A"<=i<="Z":
       ls1=ls1+1
    elif i ==" ":
        ls2=ls2+1
    elif "0"<=i<="9":
        ls3=ls3+1
    else:
        ls4=ls4+1
print(ls1,ls2,ls3,ls4) 

