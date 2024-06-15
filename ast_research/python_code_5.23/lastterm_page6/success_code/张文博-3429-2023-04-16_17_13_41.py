a=input()
j,k,l,z=0,0,0,0
for x in a:
    if ord("A")<=ord(x)<=ord("z"):
        j=j+1
    if x==" ":
        k=k+1
    elif ord("0")<=ord(x)<=ord("9"):
        l=l+1
    else:
        z=z+1
print(j,k,l,z,end=" ")

