a=eval(input())
sp=[3,4,5]
s=[6,7,8]
f=[9,10,11]
w=[12,1,2]
if a<1 or a>12:
    print("error")
elif a in sp:
    print("spring")
elif a in s:
    print("summer")
elif a in f:
    print("fall")
elif a in sp:
    print("winter")
