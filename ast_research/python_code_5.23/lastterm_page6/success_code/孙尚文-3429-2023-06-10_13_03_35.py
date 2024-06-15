a="abcd 1 2 3 4!@#$$%^"
lst=[]
for i in a:
    lst.append(i)
lst2=[0,0,0,0]
for i in lst:
    if "a"<=i<="z" or "A"<=i<="Z":
        lst2[0]+=1
    elif i==" ":
        lst2[1]+=1
    elif i in ["1","2","3","4","5","6","7","8","9"]:
        lst2[2]+=1
    else:
        lst2[3]+=1
print(" ".join(map(str,lst2)))
