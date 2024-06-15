n=input()
a=[]
b=[]
for i in range(len(n)):
    if n[i].isnumeric():
        a.append(n[i])
        if len(a)>=len(b):
            b=a.copy()
    else:
        a=[]
if len(b)>0:
    print(''.join(b))
else:
    print('No digits')    
