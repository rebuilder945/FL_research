s=input()
i=0
lst=list(s)
ls1=[]
ls2=[]
ls3=[]
ls4=[]
if len(s)>=8:
    i+=1
for x in lst:
    if x in "0123456789":
        ls1.append(x)
    elif x in "qwertyuiopasdfghjklzxcvbnm":
        ls2.append(x)
    elif x in "QWERTYUIOPASDFGHJKLZXCVBNM":
        ls3.append(x)
    elif x in "~!@#$%^&*()_=-/,.?<>;:[]}{\|": 
        ls4.append(x)
if ls1!=[]:
    i+=1
if ls2!=[]:
    i+=1
if ls3!=[]:
    i+=1
if ls4!=[]:
    i+=1
print(i)
