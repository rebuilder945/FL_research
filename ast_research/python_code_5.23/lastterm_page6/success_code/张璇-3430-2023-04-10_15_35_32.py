a=[]
for x in range(2):
    a.append("winter")
for x in range(3):
    a.append("spring")
for x in range(3):
    a.append("summer")
for x in range(3):
    a.append("autumn")
a.append("winter")
e=eval(input())
if 0<e<13:
    print(a[e-1])
else :
    print("error")

