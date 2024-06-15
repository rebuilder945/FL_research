a=input() or "None"
if a=="None":
    print("None")
else:
    for i in a:
        if a.count(i)==1:
            print(i)
            break
           
