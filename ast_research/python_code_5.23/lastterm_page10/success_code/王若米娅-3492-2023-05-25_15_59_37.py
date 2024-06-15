if input()=="":
    print("None")
else:
    ls=list(x for x in input())
    for x in ls:
        if ls.count(x)==1:
            print(x)
            break


    
