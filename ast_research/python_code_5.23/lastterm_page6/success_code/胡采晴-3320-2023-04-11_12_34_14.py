leng = int(input("please input length:"))
wid = int(input("please input width:"))
if leng<=0:
    print("illegal data")
elif wid<=0:
    print("illegal data")
elif leng==wid:
    print("It's a square")
elif leng!=wid:
    print("It's a rectangle")
