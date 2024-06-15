mon = int(input())
if 2 < mon < 6 :
    print("spring")
elif 5 < mon < 9 :
    print("summer")
elif 8 < mon < 12 :
    print("autumn")
elif mon == 12 or 0 < mon < 3 :
    print("winter")
else:
    print("error")
