n=input() or "None"
if n=="None":
    print(n)
else:    
    for i in n:
        if n.count(i)==1:
            print(i)
            break

