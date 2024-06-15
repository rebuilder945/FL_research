set1 = {x for x in range(1,11)}
set2 = {x for x in range(11,19)}
set3 = {x for x in range(19,29)}
set4 = {x for x in range(29,37)}
a = int(input())
if (a in set1) or (a in set3):
    if a % 2 == 0:
        print("black")
    else:
        print("red")
elif (a in set2) or (a in set4):
    if a % 2 == 0:
        print("red")
    else:
        print("black")
elif a == 0:
    print("green")
else:
    print("error")            
               

