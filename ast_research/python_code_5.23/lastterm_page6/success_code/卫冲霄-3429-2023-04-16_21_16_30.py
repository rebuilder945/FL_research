zifu=input()
l1=0
l2=0
l3=0
l4=0
for i in zifu:
    if "a"<=i<="z" or "A"<=i<="Z":
        l1+=1
    elif i==" ":
        l2+=1
    elif "0"<=i<="9":
        l3+=1
    else:
        l4+=1
print(l1,l2,l3,l4,end="")

