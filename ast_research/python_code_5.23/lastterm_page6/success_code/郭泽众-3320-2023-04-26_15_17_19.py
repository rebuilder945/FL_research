leng = int(input())
wid = int(input())
if leng == wid > 0:
    print("It's a square")
elif leng != wid and leng > 0 and wid > 0:
    print("It's a rectangle")
else:
    print("illegal data")
