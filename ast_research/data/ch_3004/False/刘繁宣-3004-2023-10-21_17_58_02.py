ls=eval(input())
ls2=[]
ls3=[]
for i in ls:
    for x in range(1,i):
        if i%x == 0:
            ls2.append(i)
for i in range(len(ls)):
    if not ls[i] in ls2:
        ls3.append(ls[i])
print([2]+ls3) 
print(ls2)
        
