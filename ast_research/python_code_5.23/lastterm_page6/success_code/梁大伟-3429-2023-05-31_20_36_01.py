l=input()
y=0
k=0
s=0
q=0
l.lower()
for i in l:
    if ord(i) in range(97,123):
        y+=1
    elif ord(i) in range(48,58):
        s+=1
    elif i==' ':
        k+=1
    else:
        q+=1
print(y,k,s,q)
