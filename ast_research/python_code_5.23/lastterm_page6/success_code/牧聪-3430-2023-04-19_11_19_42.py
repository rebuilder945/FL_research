weather=[3,4,5,6,7,8,9,10,11,12,1,2]
a=int(input())
if a not in weather:
    print("error")
elif a in weather[:3]:
    print("spring")
elif a in weather[3:6]:
    print("summer")
elif a in weather[6:9]:
    print("autumn")
else:
    print("winter")

