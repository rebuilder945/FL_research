a1=input()
b1=0
b2=0
b3=0
b4=0
for i in a1:
    if 'a'<=i<='z':
        b1+=1
    if i==" ":
        b2+=1
    if '1'<=i<='9':
        b3+=1
    else:
        b4+=1
print(b1,end=" ")
print(b2,end=" ")
print(b3,end=" ")
print(b4,end=" ")

        
