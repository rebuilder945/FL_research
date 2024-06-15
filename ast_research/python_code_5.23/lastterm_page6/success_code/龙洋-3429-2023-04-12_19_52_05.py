zzz=input()
n1=0
n2=0
n3=0
for x in zzz:
    if "a"<=x<='z' or 'A'<=x<='Z':
        n1+=1
    elif ' '==x:
        n2+=1
    elif "0"<=x<='9':
        n3+=1
n4=len(zzz)-n1-n2-n3
print(n1,n2,n3,n4)


