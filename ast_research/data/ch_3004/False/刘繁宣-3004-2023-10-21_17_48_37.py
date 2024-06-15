ls=eval(input())
ls2=[]
ls3=[]
for i in ls:
    for x in range(1,i):
        if i%x != 0:
            ls2.append(i)
for i in range(len(ls2)):
    if not ls2[i] in ls3:
        ls3.append(ls2[i])
print(ls3) 
        
