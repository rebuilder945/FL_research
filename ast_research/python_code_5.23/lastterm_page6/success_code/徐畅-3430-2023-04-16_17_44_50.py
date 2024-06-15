n=eval(input())
if n not in range(1,13):
    print("error")
if n in range(3,6):
    print("spring")
if n in range(6,9):
    print("summer")
if n in range(9,12):
    print("autumn")
if n in [1,2,12]:
    print("winter")
