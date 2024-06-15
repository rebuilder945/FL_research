str=input()
x=0
j=0
k=0
n=0
for i in str:
    if "0"<=i<="9":
        x+=1
    elif "A" <=i<="Z" or "a"<=i<="z":
        j+=1
    elif i==" ":
        k+=1
    else:
        n+=1
print(j,k,x,n)
