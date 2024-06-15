leng = int(input())
wid = int(input())
if leng<=0:
    print("illegal data")
elif wid<=0:
    print("illegal data")
elif leng==wid:
    print("It's a square")
elif leng!=wid:
    print("It's a rectangle")
