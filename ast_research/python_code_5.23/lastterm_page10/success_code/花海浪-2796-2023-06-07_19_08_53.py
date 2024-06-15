a=input()
b=[]
c=[]
for i in range(len(a)):
    if "0"<=a[i]<="9":
        b.append(a[i])
        if len(b)>=len(c):
            c=b.copy()
    else:
        b=[]
if len(c)>0:
    print("".join(c))
else:
    print("No digts")

