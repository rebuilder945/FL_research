a=int(input())
b=str(a)
if a<1 or a>12:
    print("error")
else:
    spring=["3","4","5"]
    summer=["6","7","8"]
    autumn=["9","10","11"]
    winter=["12","1","2"]
    if b in spring:
        print("spring")
    if b in summer:
        print("summer")
    if b in autumn:
        print("autumn")
    if b in winter:
        print("winter")
