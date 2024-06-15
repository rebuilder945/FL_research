m=input()
a=[]
b=[]
for i in range(len(m)):
    if "0"<m[i]<="9":
        a.append(m[i])
        if len(a)>=len(b):
            b=a.copy()
    else:
        a=[]
if len(b)>0:
    print("".join(b))
else:
    print("No digits")
