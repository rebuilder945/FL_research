str1=input()
if str1=="":
    print("None")
else:
    ls=list(x for x in str1)
    for x in ls:
        if ls.count(x)==1:
            print(x)
            break


    
