yuefen= eval(input())
if yuefen in range(3,6):
    print("spring")
if yuefen in range(6,9):
    print("summer")
if yuefen in range(9,12):
    print("autumn")
if yuefen in [1,2,12]:
    print("winter")
if yuefen not in range(1,13):
     print("error")
