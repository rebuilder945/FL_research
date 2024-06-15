a=input()
ls1=[]
ls2=[]
ls3=[]
for i in a:
    if i in'abcdefghijklmnopqrstuvwxyz':
        ls1.append(i)
for i in a:
    if i==' ':
        ls2.append(i)
for i in a:
    if'0'<=i<='9':
        ls3.append(eval(i))

print(len(ls1),len(ls2),len(ls3),len(a)-len(ls1)-len(ls2)-len(ls3))


