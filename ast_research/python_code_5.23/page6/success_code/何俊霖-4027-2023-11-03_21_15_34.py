x=input()
sum=0
c=0
while x!='#':
    sum+=int(x)
    c+=1
    x=input()
    if x == '#':
        print(c,sum)
        break
