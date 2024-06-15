a=input()
la=len(a)
s=""
slong=""
for i in range(la):
    for j in range(la-i):
        b=a[i:i+j+1]
        if b.isdigit():
            s=b
        if len(s)>=len(slong):
            slong=s
if len(slong)!=0:
    print(slong)
else:
    print("No digits")
