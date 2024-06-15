l=list(input())
l1=[]
l2=[]
l3=[]
l4=[]
for i in l:
    if "a"<=i<="z" or "A"<=i<="Z":
        l1.append(i)
    elif i==" ":
        l2.append(i)
    elif "0"<=i<="9":
        l3.append(i)
    else:
        l4.append(i)
print(len(l1),len(l2),len(l3),len(l4))
