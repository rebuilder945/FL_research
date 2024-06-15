str1=input()
ls=[]
maxls=[]
for x in str1:
    if "0"<=x<="9":
        ls.append(x)
        if len(ls)>=len(maxls):
            maxls=ls.copy()
        else:
            pass
    else:
        ls.clear()
s=""
if len(maxls)==0:
    print("No digits")
else:
    for x in maxls:
        s=s+str(x)
    print(s)

    

