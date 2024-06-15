a=input()
b=list("zxcvbnmlkjhgfdsapoiuytrewqQWERTYUIOPLKJHGFDSAZXCVBNM@#$%^&*()_+{}-=/")
for x in list(a):
    if x in b:
        a=a.replace(x,"*")
c=a.split("*")

d=[]
for i in c:
    if i!='':
        d.append(i)
e=[]
for i in d:
    if len(i)==max(len(i) for i in d):
        e.append(i)
print(e[-1])


