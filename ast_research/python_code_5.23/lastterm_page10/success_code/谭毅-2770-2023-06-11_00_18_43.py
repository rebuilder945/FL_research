a=list(eval(input()))
b=list(eval(input()))
ls1=[]
ls2=[]
for x in a:
    if x in b:
        ls1.append(x)
    else:
        continue
for y in b:
    if y in a:
        ls2.append(x)
    else:
        continue   
ls1.sort()
ls2.sort()
if ls1==ls2:
    print('True')
else:
    print('False')
