ls=input()
ls1=[]
ls2=[]
ls3=[]
other=0
for i in ls:
    if i.isalpha():
        ls1.append(i)
    if i.isspace():
        ls2.append(i)
        print(len(ls2))
    if i.isdigit():
        ls3.append(i)
        print(len(ls3))
    else:
        other += 1
print(len(ls1),len(ls2),len(ls3),other)


