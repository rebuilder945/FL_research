a = input()
ls1 = []
ls2 = []
ls3 = []
ls4 = []
ls5 = []
for x in a:
    if x.isalpha():
        if x.islower():
            ls1.append(x)
        elif x.isupper():
            ls2.append(x)
    elif x.isnumeric():
        ls3.append(x)
    elif x in ("~","!","@","#","$","%","^","&","*","(",")","_","=","-","/",",",".","?","<",">",";",":","[","]","{","}","|","\""):
        ls4.append(x)
c = 0
if ls1!=[]:
    c+=1
if ls2!=[]:
    c+=1
if ls3!=[]:
    c+=1
if ls4!=[]:
    c+=1
if len(a)>=8:
    c+=1
print(c)
