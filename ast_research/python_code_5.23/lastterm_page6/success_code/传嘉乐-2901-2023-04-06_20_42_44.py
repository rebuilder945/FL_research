b=0
c=0
while True:
    a=input()
    if a == "#":
        break
    else:
        b+=1
        c+=int(a)
print(b,c,end=' ')
