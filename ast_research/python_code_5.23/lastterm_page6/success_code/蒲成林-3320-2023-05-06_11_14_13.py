le = float(input())
sa = float(input())
if le <= 0 or sa <= 0:
    print("illegal data")
else:
    if le == sa:
        print("It's a square")
    if le != sa:
        print("It's a rectangle")

