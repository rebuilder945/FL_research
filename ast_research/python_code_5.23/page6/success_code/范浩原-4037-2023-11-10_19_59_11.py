a=[3,4,5]
b=[6,7,8]
c=[9,10,11]
d=[12,1,2]
e=input()
if e in a:
    print("spring")
    if e in b:
        print("summer")
        if e in c :
            print("autumn")
            if e in d:
                print("winter")
            else:
                print("error")
