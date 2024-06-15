ls=eval(input())
ls1=[]
for s in ls:
    for i in range (2,s):
        if(s % i==0):
            break
        else:
            ls1.append(s)
print(set(ls1))
            
