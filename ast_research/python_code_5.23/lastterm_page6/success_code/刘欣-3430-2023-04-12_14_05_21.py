yuefen = int(input())
if 2< yuefen <6:
    print("spring")
elif 5<yuefen<9:
    print("summer")
elif 8<yuefen<12:
    print("autumn")
elif yuefen==12 or 0<yuefen<3:
    print("winter")
else:
    print("error")
