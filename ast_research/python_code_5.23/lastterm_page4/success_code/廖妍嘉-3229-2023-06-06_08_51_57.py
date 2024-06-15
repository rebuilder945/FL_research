ls=eval(input())
ls2=[]
for i in ls:
    if ls.count(i)==1:
        ls2.append(i)
    ls2.sort()
if ls2==[]:
    print("False")
else:
    print(''.join(str(i) for i in ls2))

