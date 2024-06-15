str=input()
ls=str.split()
str2=input()
ls2=str2.split()
a=int(ls2[0])
b=int(ls2[1])
ls[a],ls[b]=ls[b],ls[a]
print(ls)
    
