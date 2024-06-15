s=0
m=1
while True:
    n=input()
    if n!= "#":
        s+=int(n)
        m+=1
    else:
        break
print(s,m)

