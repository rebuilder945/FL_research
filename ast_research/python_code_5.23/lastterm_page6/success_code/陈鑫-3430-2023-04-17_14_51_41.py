a=eval(input())
if a<1 or a >12:
    print("error")
else:
    if 2<a<5:
        print("spring")
    if 5<a<9:
        print("summer")
    if 8<a<12:
        print("autumn")
    if a==1 or a==2 or a==12:
        print("winter")
        
