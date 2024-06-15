a=input()
alst1=[]
for i in range(97,123):
    alst1.append(chr(i))
alst2=[]
for i in range(65,91):
    alst2.append(chr(i))
for x in a:
    if x.isalpha():
        if x.islower():
            x=alst1[26-(alst1.index(x)+1)]
            print(x,end='')
        if x.isupper():
            x=alst2[26-(alst2.index(x)+1)]
            print(x,end='')
    else:
            print(x,end='')
