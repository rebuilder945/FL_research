str=input()
i=0
j=0
k=0
n=0
for i in str:
    if type(i)==type(1):
        i+=1
    elif "A" <=i<="Z" or "a"<=i<="z":
        j+=1
    elif i==" ":
        k+=1
    else:
        n+=1
print(j,k,i,n)
