ls=eval(input())
ls=ls.sort()
ls2=[]
for i in range(len(ls)):
    if ls[i]  not in ls[i:len(ls)]:
        ls2.append(ls[i])
    if ls2==[]:
        print("False")
    else:
        print(ls2)

