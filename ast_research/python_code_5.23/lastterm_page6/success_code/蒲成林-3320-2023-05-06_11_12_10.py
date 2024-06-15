le = float(input())
sa = float(input())
if le == sa:
    print("It's a square")
elif le != sa:
    print("It's a rectangle")
elif le <= 0 or sa <= 0:
    print("illegal data")
