str=input()
ls1=str.split(",")
ls2=eval(input())
d=len(ls2)
ls3=[]
i=0
for x in ls1:
    ls4=[]
    if i<d:
        ls3.append(x)
        ls3.append(ls2[i])
        ls4.append(ls3)
        i+=1
print(ls4)
    

