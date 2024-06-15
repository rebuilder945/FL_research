ls=list(eval(input()))
b,c=eval(input())
if b<len(ls):
    for i in ls[:]:
        if ls.index(i)==b:
                ls.append(i*c)
        else:
            pass
    print(ls)
else:
    print("error")
        
