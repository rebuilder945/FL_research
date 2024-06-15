ls=eval(input())
a=max(ls)
b=min(ls)
ls2=[a,b]
ls3=[]
for i in ls:
    if i not in ls2:
        ls3.append(i)
print(ls3)

            


        
