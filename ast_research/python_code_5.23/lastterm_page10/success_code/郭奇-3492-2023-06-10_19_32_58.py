a=input()
a=list(a)

if a==[]:
    print("None")
else:
    for i in a:
        if a.count(i)==1:
            print(i)
            break
    else:
        print("None")
