ls=eval(input())
ls1=[]
for i in range(len(ls)):
    if ls.count(ls[i])==1:
        ls1.append(ls[i]) 
        ls1.sort()
        print(ls1)
        break
    elif ls.count(ls[i])!=1:
        print(False)
        break
