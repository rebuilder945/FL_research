n=eval(input())
a=[x for x in range(1,13)]
if n not in a:
    print("error")
else:
    if n in a[2:5]:
        print("spring")
    if n in a[5:9]:
        print("summer")
    if n in a[9:12]:
        print("autumn")
    else:
        print("winter")
