length = float(input().strip())  
width = float(input().strip())  
if width<=0 or length<=0:
    print("illegal data")
elif length==width:
    print("It's a square")
else:
    print("It's a rectangle")

