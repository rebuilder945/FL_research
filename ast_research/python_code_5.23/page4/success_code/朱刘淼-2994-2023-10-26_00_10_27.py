ls=list(eval(input()))
b,c=eval(input())
if b<len(ls):
    for i in ls[:]:
        if ls.index(i)==b:
            for x in range(c):
                ls.append(i)
        else:
            pass
    print(ls)
else:
    print("error")
        
