n=int(input())
if n<1 or n>12:
    print("error")
elif 2<n<6:
    print("spring")
elif 5<n<9:
    print("summer")
elif 8<n<12:
    print("autumn")
elif n==12 or n==1 or n==2:
    print("winter")

