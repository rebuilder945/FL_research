b=0
c=0
d=[]
while True:
    a=input()
    if a=="#":
        break
    else:
        b+=1
        c+=int(a)
d.append(b)
d.append(c)
print(" ".join(map(str,d)))
