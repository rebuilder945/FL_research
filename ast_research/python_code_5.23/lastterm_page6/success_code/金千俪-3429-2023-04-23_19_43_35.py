a=input()
f1=0
f2=0
f3=0
f4=0
for i in a:
    if "a"<=i<="z" or "A"<=i<="Z":
        f1+=1
    elif i==" ":
        f2+=1
    elif "0"<=i<="9":
        f3+=1
    else:
        f4+=1
print(f1,f2 ,f3 ,f4,sep=" ")


