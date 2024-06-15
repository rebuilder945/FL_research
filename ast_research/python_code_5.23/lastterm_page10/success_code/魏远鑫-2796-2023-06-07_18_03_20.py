s=input()
tem=[]
max=[]
for i in range(len(s)):
    if "0"<=s[i]<="9":
        tem.append(s[i])
        if len(tem)>=len(max):
            max=tem
    else:
        tem=[]
if len(max)>0:
    print("".join(max))
else:
    print("No digits")
