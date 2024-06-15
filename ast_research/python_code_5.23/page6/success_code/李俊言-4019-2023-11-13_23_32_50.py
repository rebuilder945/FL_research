a=input()
c=""
for x in a:
    b=str((int(x)+5)%10)
    c=c+b
c=list(c)
c.reverse()
for i in c:   
 print(i,end='')
