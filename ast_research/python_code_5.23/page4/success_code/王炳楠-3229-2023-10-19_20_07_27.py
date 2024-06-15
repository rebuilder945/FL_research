ls=eval(input())
ls1=[]
for i in range(len(ls)):
    if i==len(ls):
        if ls[i] not in ls[:i:1]:
            ls1.append(ls[i])
    elif i==0:
        if ls[i] not in ls[1::1]:
            ls1.append(ls[i])       
    else:
        if ls[i] not in ls[i+1::1] and ls[i] not in ls[i-1::-1] :
            if ls[i] not in ls1:
                ls1.append(ls[i])
ls1.sort()
if ls1==[]:
    print("False")
else:
    print(",".join(ls1))
        



