s = input()
l = []
long=[]
for i in s:
    if "0"<=i<="9":
        l.append(i)
        if len(l)>=len(long):
            long=l.copy()
    else:
        l=[]
if len(long)>0:
    print("".join(long))
else:
    print("No digits")
