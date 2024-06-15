b=0
c=0
while True:
    a=eval(input())
    if a == "#":
        break
    else:
        b+=1
        c+=a
print(b,c,end=' ')
