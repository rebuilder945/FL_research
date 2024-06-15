ls=eval(input())
for i in range(len(ls)):
    if ls[i] == 0:
        a=ls.pop(i)
        ls.append(0)
    

