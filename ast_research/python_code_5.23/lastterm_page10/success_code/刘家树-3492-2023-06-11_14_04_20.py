a=input() or "None"
if a=="None":
    print("None")
else:   
    l=list(a)
    b=[]
    for x in l:
        c=l.count(x)
        if c==1:
            print(x)
            break
    


