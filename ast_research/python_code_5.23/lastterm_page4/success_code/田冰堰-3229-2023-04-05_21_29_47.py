ls=eval(input())
ls.sort()
save=[]
for i in ls:
    if(ls.count(i))==1:
        save.append(i)
        print(save)
    else:
        print("False")
