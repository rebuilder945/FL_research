n=input()
y,s,q=0,0,0
for x in n:
    k=n.count(' ')
    if 'a'<=x<='z':
        y+=1
    elif '0'<=x<='9':
        s+=1
    elif  (not(('a'<=x<='z')and('0'<=x<='9')))and x!=" ":
        q+=1
print(y,k,s,q,sep=" ")
