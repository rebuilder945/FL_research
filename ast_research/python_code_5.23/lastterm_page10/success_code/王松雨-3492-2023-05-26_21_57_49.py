a=input() or "None"
if a=="None":
    print("None")
else:
    for i in a:
        lst=[]
        if a.count(i)==1:
            print(i)
            break
           
