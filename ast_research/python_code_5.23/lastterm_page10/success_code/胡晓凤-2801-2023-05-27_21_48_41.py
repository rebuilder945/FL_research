a=input()
print(a)
m1=[]
m2=[]
m3=[]
m4=[]
for i in a:
    if "0"<=i<="9":
        m1.append(i)
    elif "a"<=i<="z":
        m2.append(i)
    elif "A"<=i<="Z":
        m3.append(i)
    else:
        m4.append(i)
s=0
if m1!=[]:
    s=s+1
    if m2!=[]:
        s=s+1
        if m3!=[]:
            s+=1
            if len(a)>=8:
                s+=1
                if m4!=[]:
                    s+=1
print(s)
