l=input()
y=0
k=0
s=0
q=0
for i in l:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
        y+=1
    elif i in '0123456789':
        s+=1
    elif i==' ':
        k+=1
    else:
        q+=1
print(y,k,s,q)
