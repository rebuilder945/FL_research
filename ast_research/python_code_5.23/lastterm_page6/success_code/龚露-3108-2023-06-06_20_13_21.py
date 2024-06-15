a=input()
ls1=[]
ls2=[]
ls3=[]
ls4=[]
for x in a:
    if x.isalpha():
        ls1.append(x)
    elif x==' ':
        ls2.append(x)
    elif x.isdigit():
        ls3.append(x)
    else:
        ls4.append(x)
print(len(ls1),len(ls2),len(ls3),len(ls4))
    
